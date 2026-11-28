// JGraphT file importers as a black box for the io_formats oracle
// (io_formats_jgrapht_oracle.py): CSV (edge list, adjacency list, matrix) and
// TSPLIB. Reads the index file written by the Python script and prints, per
// case, the vertices in the graph's own order and its edges:
//   case <index>
//   V <name>
//   E <source> <target> <weight>
// Index line: <kind> <file> <directed 0|1> <weights 0|1> <node ids 0|1>
// kinds: csv_edges, csv_adjlist, csv_matrix, tsplib.
import org.jgrapht.Graph;
import org.jgrapht.graph.DefaultWeightedEdge;
import org.jgrapht.graph.DirectedWeightedPseudograph;
import org.jgrapht.graph.SimpleWeightedGraph;
import org.jgrapht.graph.WeightedPseudograph;
import org.jgrapht.nio.csv.CSVFormat;
import org.jgrapht.nio.csv.CSVImporter;
import org.jgrapht.nio.tsplib.TSPLIBImporter;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.function.Supplier;

public class IoOracle {
  static class Numbers implements Supplier<Integer> {
    int next = 0;
    public Integer get() { return next++; }
  }

  static void print(PrintStream out, int index, Graph<?, DefaultWeightedEdge> g) {
    out.println("case " + index);
    for (Object v : g.vertexSet()) out.println("V " + v);
    for (DefaultWeightedEdge e : g.edgeSet())
      out.println("E " + g.getEdgeSource(e) + " " + g.getEdgeTarget(e) + " " + g.getEdgeWeight(e));
  }

  public static void main(String[] args) throws Exception {
    String dir = args[0];
    PrintStream out = new PrintStream(args[1], "UTF-8");
    try (BufferedReader index = new BufferedReader(new FileReader(dir + "/index.txt"))) {
      String line;
      int n = 0;
      while ((line = index.readLine()) != null) {
        String[] f = line.split(" ");
        String text = new String(Files.readAllBytes(Paths.get(dir, f[1])), StandardCharsets.ISO_8859_1);
        boolean directed = f[2].equals("1"), weights = f[3].equals("1"), ids = f[4].equals("1");
        if (f[0].equals("tsplib")) {
          SimpleWeightedGraph<Integer, DefaultWeightedEdge> g = new SimpleWeightedGraph<>(DefaultWeightedEdge.class);
          g.setVertexSupplier(new Numbers());
          new TSPLIBImporter<Integer, DefaultWeightedEdge>().importGraph(g, new java.io.StringReader(text));
          print(out, n++, g);
          continue;
        }
        Graph<String, DefaultWeightedEdge> g = directed
            ? new DirectedWeightedPseudograph<>(DefaultWeightedEdge.class)
            : new WeightedPseudograph<>(DefaultWeightedEdge.class);
        CSVFormat format = f[0].equals("csv_edges") ? CSVFormat.EDGE_LIST
            : f[0].equals("csv_adjlist") ? CSVFormat.ADJACENCY_LIST : CSVFormat.MATRIX;
        CSVImporter<String, DefaultWeightedEdge> importer = new CSVImporter<>(format, ',');
        importer.setVertexFactory(s -> s);
        importer.setParameter(CSVFormat.Parameter.EDGE_WEIGHTS, weights);
        importer.setParameter(CSVFormat.Parameter.MATRIX_FORMAT_NODEID, ids);
        importer.setParameter(CSVFormat.Parameter.MATRIX_FORMAT_ZERO_WHEN_NO_EDGE, true);
        importer.importGraph(g, new java.io.StringReader(text));
        print(out, n++, g);
      }
    }
    out.close();
  }
}
