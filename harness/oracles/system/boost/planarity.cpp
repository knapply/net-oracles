// Boost Graph Library planarity driver: black-box use of the published
// headers (boyer_myrvold_planarity_test, make_connected,
// make_biconnected_planar, make_maximal_planar, planar_canonical_ordering,
// chrobak_payne_straight_line_drawing).
//   planarity <input> <output>
// input:  fixture count, then per fixture: name n m followed by m pairs u v
//         (the simple undirected graph underlying the fixture)
// output: per fixture a block
//   fixture <name>
//   planar 0|1
//   ring <v> <k> <neighbours in embedding order>      (planar, every node)
//   point <v> <x> <y>                                  (planar, n >= 3)
//   kuratowski <u> <v>                                 (non-planar, per edge)
//   error <text>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/boyer_myrvold_planar_test.hpp>
#include <boost/graph/chrobak_payne_drawing.hpp>
#include <boost/graph/make_biconnected_planar.hpp>
#include <boost/graph/make_connected.hpp>
#include <boost/graph/make_maximal_planar.hpp>
#include <boost/graph/planar_canonical_ordering.hpp>
#include <boost/version.hpp>
#include <fstream>
#include <iostream>
#include <iterator>
#include <string>
#include <utility>
#include <vector>

using namespace boost;

typedef adjacency_list<vecS, vecS, undirectedS, no_property, property<edge_index_t, int>> PG;
typedef graph_traits<PG>::edge_descriptor Edge;
typedef std::vector<Edge> Rot;
typedef std::vector<Rot> Storage;
typedef iterator_property_map<Storage::iterator, property_map<PG, vertex_index_t>::type> EmbMap;

static void reindex(PG& g) {
  int k = 0;
  graph_traits<PG>::edge_iterator it, end;
  for (boost::tie(it, end) = edges(g); it != end; ++it) put(get(edge_index, g), *it, k++);
}

static bool embed(PG& g, EmbMap& emb) {
  return boyer_myrvold_planarity_test(boyer_myrvold_params::graph = g,
                                      boyer_myrvold_params::embedding = emb);
}

int main(int argc, char** argv) {
  std::ifstream in(argv[1]);
  std::ofstream out(argv[2]);
  int count;
  in >> count;
  for (int c = 0; c < count; c++) {
    std::string name;
    int n, m;
    in >> name >> n >> m;
    PG g(n);
    for (int i = 0; i < m; i++) {
      int u, v;
      in >> u >> v;
      add_edge(u, v, g);
    }
    reindex(g);
    out << "fixture " << name << "\n";
    try {
      Storage storage(n);
      EmbMap emb(storage.begin(), get(vertex_index, g));
      if (!embed(g, emb)) {
        out << "planar 0\n";
        std::vector<Edge> cert;
        PG h(g);
        boyer_myrvold_planarity_test(boyer_myrvold_params::graph = h,
                                     boyer_myrvold_params::kuratowski_subgraph = std::back_inserter(cert));
        for (const Edge& e : cert) out << "kuratowski " << source(e, h) << " " << target(e, h) << "\n";
        continue;
      }
      out << "planar 1\n";
      for (int v = 0; v < n; v++) {
        out << "ring " << v << " " << storage[v].size();
        for (const Edge& e : storage[v]) out << " " << (source(e, g) == (unsigned)v ? target(e, g) : source(e, g));
        out << "\n";
      }
      if (n < 3) continue;
      make_connected(g);
      reindex(g);
      embed(g, emb);
      make_biconnected_planar(g, emb);
      reindex(g);
      embed(g, emb);
      make_maximal_planar(g, emb);
      reindex(g);
      embed(g, emb);
      std::vector<graph_traits<PG>::vertex_descriptor> ordering;
      planar_canonical_ordering(g, emb, std::back_inserter(ordering));
      struct Coord { std::size_t x, y; };
      std::vector<Coord> pts(n);
      iterator_property_map<std::vector<Coord>::iterator, property_map<PG, vertex_index_t>::type>
          drawing(pts.begin(), get(vertex_index, g));
      chrobak_payne_straight_line_drawing(g, emb, ordering.begin(), ordering.end(), drawing);
      for (int v = 0; v < n; v++) out << "point " << v << " " << pts[v].x << " " << pts[v].y << "\n";
    } catch (std::exception& e) {
      std::string text = e.what();
      for (char& ch : text) if (ch == '\n') ch = ' ';
      out << "error " << text << "\n";
    }
  }
  std::cout << "boost " << BOOST_LIB_VERSION << "\n";
  return 0;
}
