// Boost Graph Library random layout driver: black-box use of the published
// headers (random_graph_layout over a rectangle_topology).
//   random_layout <output> <n> [<n> ...]
// For every node count n it writes four layouts in the order the oracle asks
// for them: seed 7 on a path, seed 7 on a path again, seed 7 on a graph with
// no edges, seed 8 on a path; then (n = 20000 only) seed 1 with no edges. The
// path stands for the fixture's own edges: Boost's function takes the graph
// only for its node set.
// output: per layout a block
//   layout <n> <seed> <edges 0|1>
//   <x> <y>                         (n lines)
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/random_layout.hpp>
#include <boost/graph/topology.hpp>
#include <boost/random/linear_congruential.hpp>
#include <boost/version.hpp>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::undirectedS> Graph;
typedef boost::rectangle_topology<> Topology;
typedef Topology::point_type Point;

static void emit(std::ostream& out, int n, unsigned seed, bool edges) {
  Graph g(n);
  if (edges)
    for (int i = 0; i + 1 < n; ++i) boost::add_edge(i, i + 1, g);
  boost::minstd_rand gen(seed);
  Topology space(gen, -1.0, -1.0, 1.0, 1.0);
  std::vector<Point> pos(n);
  boost::iterator_property_map<std::vector<Point>::iterator,
                               boost::property_map<Graph, boost::vertex_index_t>::type>
      position(pos.begin(), get(boost::vertex_index, g));
  boost::random_graph_layout(g, position, space);
  out << "layout " << n << " " << seed << " " << (edges ? 1 : 0) << "\n";
  for (int i = 0; i < n; ++i)
    out << std::setprecision(17) << pos[i][0] << " " << pos[i][1] << "\n";
}

int main(int argc, char** argv) {
  if (argc < 3) {
    std::cerr << "usage: random_layout <output> <n>...\n";
    return 2;
  }
  std::ofstream out(argv[1]);
  for (int a = 2; a < argc; ++a) {
    int n = std::atoi(argv[a]);
    emit(out, n, 7, true);
    emit(out, n, 7, true);
    emit(out, n, 7, false);
    emit(out, n, 8, true);
    if (n == 20000) emit(out, n, 1, false);
  }
  std::cout << "boost " << BOOST_LIB_VERSION << "\n";
  return 0;
}
