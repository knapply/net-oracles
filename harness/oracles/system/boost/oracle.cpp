// Boost Graph Library oracle driver: reads the fixture corpus and writes
// golden files. Black-box use of the published headers.
//   oracle <fixtures_dir> <out_dir>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/betweenness_centrality.hpp>
#include <boost/graph/clustering_coefficient.hpp>
#include <boost/graph/closeness_centrality.hpp>
#include <boost/graph/eccentricity.hpp>
#include <boost/graph/exterior_property.hpp>
#include <boost/graph/floyd_warshall_shortest.hpp>
#include <boost/graph/kruskal_min_spanning_tree.hpp>
#include <boost/graph/strong_components.hpp>
#include <boost/graph/biconnected_components.hpp>
#include <boost/graph/page_rank.hpp>
#include <boost/version.hpp>
#include <algorithm>
#include <cmath>
#include <filesystem>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <vector>

namespace fs = std::filesystem;
using namespace boost;
static const double NANV = -999.0, INFV = -1000.0;
static fs::path outdir;
static std::ofstream errors;

struct Fx { std::string name; int n; bool directed, weighted; std::vector<int> s, t; std::vector<double> w; };

static std::string slurp(const fs::path& p) { std::ifstream f(p); std::stringstream ss; ss << f.rdbuf(); return ss.str(); }

static Fx load(const fs::path& d) {
  Fx f; f.name = d.filename().string();
  std::string meta = slurp(d / "meta.json"); std::smatch m;
  std::regex_search(meta, m, std::regex("\"n\":\\s*(\\d+)")); f.n = std::stoi(m[1]);
  std::regex_search(meta, m, std::regex("\"directed\":\\s*(true|false)")); f.directed = m[1] == "true";
  std::regex_search(meta, m, std::regex("\"weighted\":\\s*(true|false)")); f.weighted = m[1] == "true";
  std::ifstream in(d / "edges.csv"); std::string line; std::getline(in, line);
  while (std::getline(in, line)) {
    if (line.empty()) continue;
    std::stringstream ls(line); std::string a, b, c; std::getline(ls, a, ','); std::getline(ls, b, ',');
    f.s.push_back(std::stoi(a)); f.t.push_back(std::stoi(b));
    if (f.weighted) { std::getline(ls, c, ','); f.w.push_back(std::stod(c)); } else f.w.push_back(1.0);
  }
  return f;
}

static std::string fmt(double x) { std::ostringstream o; o << std::setprecision(17) << x; return o.str(); }
static double mark(double x) { return std::isnan(x) ? NANV : (std::isinf(x) || x >= std::numeric_limits<double>::max() / 2) ? INFV : x; }

static void put(const Fx& f, const std::string& v, const std::vector<std::vector<double>>& rows) {
  fs::path d = outdir / f.name; fs::create_directories(d);
  std::ofstream o(d / (v + ".csv")); o << "value\n";
  for (auto& r : rows) { for (size_t i = 0; i < r.size(); i++) o << (i ? " " : "") << fmt(r[i]); o << "\n"; }
}
static void put1(const Fx& f, const std::string& v, const std::vector<double>& xs) {
  std::vector<std::vector<double>> rows; for (double x : xs) rows.push_back({x}); put(f, v, rows);
}

template <class G> struct Run {
  const Fx& f; G g; int n;
  Run(const Fx& fx, bool useW) : f(fx), g(fx.n), n(fx.n) {
    for (size_t i = 0; i < fx.s.size(); i++) add_edge(fx.s[i], fx.t[i], useW ? fx.w[i] : 1.0, g);
  }
};

template <class Graph, class Fn> static void attempt(const Fx& f, const std::string& v, Fn fn) {
  try { fn(); } catch (std::exception& e) {
    std::string m = e.what(); std::replace(m.begin(), m.end(), '\n', ' ');
    errors << f.name << "\t" << v << "\t" << m << "\n";
  }
}

template <class Graph> static void all_measures(const Fx& f) {
  typedef typename graph_traits<Graph>::edge_descriptor E;
  Run<Graph> unit(f, false);
  Graph& g = unit.g; int n = f.n;
  std::unique_ptr<Run<Graph>> wr; if (f.weighted) wr.reset(new Run<Graph>(f, true));
  auto bc = [&](Graph& gg, bool weighted, bool rel) {
    std::vector<double> c(n, 0.0);
    auto cm = make_iterator_property_map(c.begin(), get(vertex_index, gg));
    if (weighted) brandes_betweenness_centrality(gg, centrality_map(cm).weight_map(get(edge_weight, gg)));
    else brandes_betweenness_centrality(gg, centrality_map(cm));
    if (rel) relative_betweenness_centrality(gg, cm);
    return c;
  };
  attempt<Graph>(f, "betweenness", [&] { put1(f, "betweenness", bc(g, false, false)); });
  attempt<Graph>(f, "betweenness_normalized", [&] { put1(f, "betweenness_normalized", bc(g, false, true)); });
  if (wr) attempt<Graph>(f, "betweenness_weighted", [&] { put1(f, "betweenness_weighted", bc(wr->g, true, false)); });

  auto dist = [&](Graph& gg) {
    typedef exterior_vertex_property<Graph, double> DP;
    typename DP::matrix_type dm(n);
    typename DP::matrix_map_type dmap(dm, gg);
    std::vector<std::vector<double>> D(n, std::vector<double>(n, std::numeric_limits<double>::infinity()));
    for (int i = 0; i < n; i++) { D[i][i] = 0; }
    BGL_FORALL_EDGES_T(e, gg, Graph) {
      int a = source(e, gg), b = target(e, gg); double w = get(edge_weight, gg, e);
      if (a != b) { D[a][b] = std::min(D[a][b], w); if (!f.directed) D[b][a] = std::min(D[b][a], w); }
    }
    return D;
  };
  auto fw = [&](Graph& gg) {  // Floyd-Warshall from the library on the edge weights
    std::vector<std::vector<double>> D(n, std::vector<double>(n));
    floyd_warshall_all_pairs_shortest_paths(gg, D, weight_map(get(edge_weight, gg)));
    return D;
  };
  auto write_dist = [&](const std::string& v, const std::vector<std::vector<double>>& D) {
    std::vector<std::vector<double>> rows;
    for (auto& r : D) { std::vector<double> x; for (double d : r) x.push_back(d >= std::numeric_limits<double>::max() / 2 ? INFV : d); rows.push_back(x); }
    put(f, v, rows);
  };
  attempt<Graph>(f, "distances", [&] { write_dist("distances", fw(g)); });
  if (wr) attempt<Graph>(f, "distances_weighted", [&] { write_dist("distances_weighted", fw(wr->g)); });

  attempt<Graph>(f, "closeness", [&] {
    typedef exterior_vertex_property<Graph, double> CP; typename CP::container_type c(n);
    typename CP::map_type cm(c, g);
    typedef exterior_vertex_property<Graph, double> DP;
    typename DP::matrix_type dm(n); typename DP::matrix_map_type dmap(dm, g);
    floyd_warshall_all_pairs_shortest_paths(g, dmap, weight_map(get(edge_weight, g)));
    all_closeness_centralities(g, dmap, cm);
    std::vector<double> r; for (int v = 0; v < n; v++) r.push_back(mark(c[v])); put1(f, "closeness", r);
  });
  attempt<Graph>(f, "eccentricity", [&] {
    typedef exterior_vertex_property<Graph, double> EP; typename EP::container_type e(n); typename EP::map_type em(e, g);
    typedef exterior_vertex_property<Graph, double> DP;
    typename DP::matrix_type dm(n); typename DP::matrix_map_type dmap(dm, g);
    floyd_warshall_all_pairs_shortest_paths(g, dmap, weight_map(get(edge_weight, g)));
    all_eccentricities(g, dmap, em);
    std::vector<double> r; for (int v = 0; v < n; v++) r.push_back(mark(e[v])); put1(f, "eccentricity", r);
    if (f.directed) put1(f, "eccentricity_out", r);
    auto rd = radius_and_diameter(g, em);
    put1(f, "radius", {mark(rd.first)}); put1(f, "diameter", {mark(rd.second)});
  });
}

template <class Graph> static void undirected_only(const Fx& f) {
  Graph g(f.n);
  for (size_t i = 0; i < f.s.size(); i++) add_edge(f.s[i], f.t[i], f.w[i], g);
  int n = f.n;
  attempt<Graph>(f, "clustering_zero", [&] {
    std::vector<double> r;
    for (int v = 0; v < n; v++) r.push_back(clustering_coefficient(g, vertex(v, g)));
    put1(f, "clustering_zero", r);
    put1(f, "average_clustering_zero", {mean_clustering_coefficient(g, make_iterator_property_map(r.begin(), get(vertex_index, g)))});
  });
  attempt<Graph>(f, "tree_mst_weight", [&] {
    std::vector<typename graph_traits<Graph>::edge_descriptor> tree;
    Graph gu(f.n); for (size_t i = 0; i < f.s.size(); i++) add_edge(f.s[i], f.t[i], 1.0, gu);
    kruskal_minimum_spanning_tree(gu, std::back_inserter(tree));
    put1(f, "tree_mst_weight", {(double)tree.size()});  // unit weights: weight == number of tree edges
  });
  if (f.weighted) attempt<Graph>(f, "tree_mst_weight_weighted", [&] {
    std::vector<typename graph_traits<Graph>::edge_descriptor> tree;
    kruskal_minimum_spanning_tree(g, std::back_inserter(tree));
    double s = 0; for (auto e : tree) s += get(edge_weight, g, e);
    put1(f, "tree_mst_weight_weighted", {s});
  });
  attempt<Graph>(f, "cut_points", [&] {
    std::vector<int> pts; articulation_points(g, std::back_inserter(pts));
    std::vector<double> r; for (int v : pts) r.push_back(v);
    std::sort(r.begin(), r.end()); r.erase(std::unique(r.begin(), r.end()), r.end());
    put1(f, "cut_points", r);
  });
}

template <class Graph> static void directed_only(const Fx& f) {
  Graph g(f.n);
  for (size_t i = 0; i < f.s.size(); i++) add_edge(f.s[i], f.t[i], f.w[i], g);
  attempt<Graph>(f, "conn_strong_partition", [&] {
    std::vector<int> comp(f.n); strong_components(g, make_iterator_property_map(comp.begin(), get(vertex_index, g)));
    std::vector<double> r(comp.begin(), comp.end()); put1(f, "conn_strong_partition", r);
  });
}

typedef property<edge_weight_t, double> EW;
typedef adjacency_list<vecS, vecS, undirectedS, no_property, EW> UG;
typedef adjacency_list<vecS, vecS, directedS, no_property, EW> DG;
typedef adjacency_list<vecS, vecS, bidirectionalS, no_property, EW> BG;

int main(int argc, char** argv) {
  fs::path fixtures = argv[1]; outdir = argv[2]; fs::create_directories(outdir);
  errors.open(outdir / "ERRORS.tsv"); errors << "fixture\tvariant\terror\n";
  std::vector<fs::path> dirs;
  for (auto& p : fs::directory_iterator(fixtures)) if (fs::exists(p.path() / "meta.json")) dirs.push_back(p.path());
  std::sort(dirs.begin(), dirs.end());
  for (auto& d : dirs) {
    Fx f = load(d);
    if (f.directed) { all_measures<DG>(f); directed_only<DG>(f); }
    else { all_measures<UG>(f); undirected_only<UG>(f); }
  }
  std::cout << "boost " << BOOST_LIB_VERSION << "\n";
  return 0;
}
