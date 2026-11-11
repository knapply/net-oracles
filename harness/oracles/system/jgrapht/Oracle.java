// JGraphT oracle driver: reads the fixture corpus and writes golden files.
// Black-box use of the published jar only.  Usage:
//   java -cp <jars>:. Oracle <fixtures_dir> <out_dir>
import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.regex.*;
import java.util.function.*;
import org.jgrapht.*;
import org.jgrapht.alg.clique.BronKerboschCliqueFinder;
import org.jgrapht.alg.connectivity.KosarajuStrongConnectivityInspector;
import org.jgrapht.alg.scoring.*;
import org.jgrapht.alg.shortestpath.DijkstraShortestPath;
import org.jgrapht.alg.spanning.KruskalMinimumSpanningTree;
import org.jgrapht.alg.shortestpath.GraphMeasurer;
import org.jgrapht.alg.interfaces.VertexScoringAlgorithm;
import org.jgrapht.graph.*;

public class Oracle {
    static final double NAN = -999.0, INF = -1000.0;
    static Path out;
    static PrintWriter errors;

    static class Fx {
        String name; int n; boolean directed, weighted; int m;
        int[] src, tgt; double[] w;
    }

    static Fx load(Path dir) throws IOException {
        Fx f = new Fx(); f.name = dir.getFileName().toString();
        String meta = Files.readString(dir.resolve("meta.json"));
        f.n = Integer.parseInt(find(meta, "\"n\":\\s*(\\d+)"));
        f.directed = find(meta, "\"directed\":\\s*(true|false)").equals("true");
        f.weighted = find(meta, "\"weighted\":\\s*(true|false)").equals("true");
        List<String> lines = Files.readAllLines(dir.resolve("edges.csv"));
        f.m = lines.size() - 1;
        f.src = new int[f.m]; f.tgt = new int[f.m]; f.w = new double[f.m];
        for (int i = 0; i < f.m; i++) {
            String[] p = lines.get(i + 1).split(",");
            f.src[i] = Integer.parseInt(p[0]); f.tgt[i] = Integer.parseInt(p[1]);
            f.w[i] = f.weighted ? Double.parseDouble(p[2]) : 1.0;
        }
        return f;
    }
    static String find(String s, String re) {
        Matcher m = Pattern.compile(re).matcher(s); m.find(); return m.group(1);
    }

    // Pseudograph (loops and parallel edges allowed); weights are 1 unless useW.
    static Graph<Integer, DefaultWeightedEdge> build(Fx f, boolean useW) {
        Graph<Integer, DefaultWeightedEdge> g = f.directed
            ? new DirectedWeightedPseudograph<>(DefaultWeightedEdge.class)
            : new WeightedPseudograph<>(DefaultWeightedEdge.class);
        for (int v = 0; v < f.n; v++) g.addVertex(v);
        for (int i = 0; i < f.m; i++) {
            DefaultWeightedEdge e = g.addEdge(f.src[i], f.tgt[i]);
            g.setEdgeWeight(e, useW ? f.w[i] : 1.0);
        }
        return g;
    }

    static double mark(double x) { return Double.isNaN(x) ? NAN : Double.isInfinite(x) ? INF : x; }

    static String fmt(double x) { return Double.toString(x); }

    static void put(Fx f, String variant, List<?> rows) throws IOException {
        Path d = out.resolve(f.name); Files.createDirectories(d);
        try (PrintWriter pw = new PrintWriter(d.resolve(variant + ".csv").toFile())) {
            pw.print("value\n");
            for (Object r : rows) {
                if (r instanceof double[]) {
                    StringBuilder sb = new StringBuilder();
                    for (double x : (double[]) r) { if (sb.length() > 0) sb.append(' '); sb.append(fmt(x)); }
                    pw.print(sb + "\n");
                } else pw.print(fmt(((Number) r).doubleValue()) + "\n");
            }
        }
    }

    static List<Double> scores(VertexScoringAlgorithm<Integer, Double> a, int n, double nanMark) {
        List<Double> r = new ArrayList<>();
        Map<Integer, Double> s = a.getScores();
        for (int v = 0; v < n; v++) {
            double x = s.get(v);
            r.add(Double.isNaN(x) ? nanMark : Double.isInfinite(x) ? INF : x);
        }
        return r;
    }

    interface Job { void run() throws Exception; }
    static void tryRun(Fx f, String variant, Job j) {
        try { j.run(); }
        catch (Throwable t) {
            errors.println(f.name + "\t" + variant + "\t" + t.getClass().getSimpleName() + ": "
                + String.valueOf(t.getMessage()).replace('\n', ' '));
        }
    }

    public static void main(String[] a) throws Exception {
        Path fixtures = Paths.get(a[0]); out = Paths.get(a[1]); Files.createDirectories(out);
        errors = new PrintWriter(out.resolve("ERRORS.tsv").toFile());
        errors.println("fixture\tvariant\terror");
        List<Path> dirs = new ArrayList<>();
        try (DirectoryStream<Path> ds = Files.newDirectoryStream(fixtures)) {
            for (Path p : ds) if (Files.exists(p.resolve("meta.json"))) dirs.add(p);
        }
        Collections.sort(dirs);
        for (Path d : dirs) {
            Fx f = load(d);
            Graph<Integer, DefaultWeightedEdge> g = build(f, false);
            Graph<Integer, DefaultWeightedEdge> gw = f.weighted ? build(f, true) : null;
            int n = f.n;
            tryRun(f, "betweenness", () -> put(f, "betweenness", scores(new BetweennessCentrality<>(g, false), n, NAN)));
            tryRun(f, "betweenness_normalized", () -> put(f, "betweenness_normalized", scores(new BetweennessCentrality<>(g, true), n, NAN)));
            if (gw != null) tryRun(f, "betweenness_weighted", () -> put(f, "betweenness_weighted", scores(new BetweennessCentrality<>(gw, false), n, NAN)));
            tryRun(f, "closeness", () -> put(f, "closeness", scores(new ClosenessCentrality<>(g, false, false), n, -1)));
            tryRun(f, "closeness_normalized", () -> put(f, "closeness_normalized", scores(new ClosenessCentrality<>(g, false, true), n, -1)));
            if (f.directed) tryRun(f, "closeness_in", () -> put(f, "closeness_in", scores(new ClosenessCentrality<>(g, true, true), n, -1)));
            if (gw != null) tryRun(f, "closeness_weighted", () -> put(f, "closeness_weighted", scores(new ClosenessCentrality<>(gw, false, true), n, -1)));
            tryRun(f, "harmonic", () -> put(f, "harmonic", scores(new HarmonicCentrality<>(g, false, false), n, -1)));
            if (f.directed) tryRun(f, "harmonic_in", () -> put(f, "harmonic_in", scores(new HarmonicCentrality<>(g, true, false), n, -1)));
            tryRun(f, "pagerank_networkx", () -> put(f, "pagerank_networkx", scores(new PageRank<>(g, 0.85, 10000, 1e-14), n, NAN)));
            if (gw != null) tryRun(f, "pagerank_weighted", () -> put(f, "pagerank_weighted", scores(new PageRank<>(gw, 0.85, 10000, 1e-14), n, NAN)));
            tryRun(f, "clustering_zero", () -> put(f, "clustering_zero", scores(new ClusteringCoefficient<>(g), n, NAN)));
            tryRun(f, "average_clustering_zero", () -> put(f, "average_clustering_zero",
                List.of(mark(new ClusteringCoefficient<>(g).getAverageClusteringCoefficient()))));
            tryRun(f, "transitivity", () -> put(f, "transitivity",
                List.of(mark(new ClusteringCoefficient<>(g).getGlobalClusteringCoefficient()))));
            tryRun(f, "coreness_all", () -> {
                Map<Integer, Integer> c = new Coreness<>(g).getScores();
                List<Double> r = new ArrayList<>();
                for (int v = 0; v < n; v++) r.add((double) c.get(v));
                put(f, "coreness_all", r);
            });
            tryRun(f, "max_cliques", () -> {
                List<double[]> rows = new ArrayList<>();
                for (Set<Integer> c : (Iterable<Set<Integer>>) () -> new BronKerboschCliqueFinder<>(g).iterator()) {
                    double[] r = c.stream().sorted().mapToDouble(Integer::doubleValue).toArray();
                    rows.add(r);
                }
                put(f, "max_cliques", rows);
                int best = 0; for (double[] r : rows) best = Math.max(best, r.length);
                put(f, "clique_number", List.of((double) best));
            });
            tryRun(f, "distances", () -> {
                DijkstraShortestPath<Integer, DefaultWeightedEdge> sp = new DijkstraShortestPath<>(g);
                put(f, "distances", matrix(sp, n));
            });
            if (gw != null) tryRun(f, "distances_weighted", () ->
                put(f, "distances_weighted", matrix(new DijkstraShortestPath<>(gw), n)));
            tryRun(f, "diameter", () -> {
                GraphMeasurer<Integer, DefaultWeightedEdge> gm = new GraphMeasurer<>(g);
                double dmt = gm.getDiameter();
                put(f, "diameter", List.of(Double.isInfinite(dmt) ? INF : dmt));
                double rad = gm.getRadius();
                put(f, "radius", List.of(Double.isInfinite(rad) ? INF : rad));
                Map<Integer, Double> ecc = gm.getVertexEccentricityMap();
                List<Double> r = new ArrayList<>();
                for (int v = 0; v < n; v++) r.add(Double.isInfinite(ecc.get(v)) ? INF : ecc.get(v));
                put(f, "eccentricity", r);
                if (f.directed) put(f, "eccentricity_out", r);
            });
            if (!f.directed) {
                tryRun(f, "tree_mst_weight", () -> put(f, "tree_mst_weight",
                    List.of(new KruskalMinimumSpanningTree<>(g).getSpanningTree().getWeight())));
                if (gw != null) tryRun(f, "tree_mst_weight_weighted", () -> put(f, "tree_mst_weight_weighted",
                    List.of(new KruskalMinimumSpanningTree<>(gw).getSpanningTree().getWeight())));
            } else {
                tryRun(f, "conn_strong_partition", () -> {
                    List<Set<Integer>> comps = new KosarajuStrongConnectivityInspector<>(g).stronglyConnectedSets();
                    double[] id = new double[n];
                    for (int c = 0; c < comps.size(); c++) for (int v : comps.get(c)) id[v] = c;
                    List<Double> r = new ArrayList<>(); for (double x : id) r.add(x);
                    put(f, "conn_strong_partition", r);
                });
            }
        }
        errors.close();
    }

    static List<double[]> matrix(DijkstraShortestPath<Integer, DefaultWeightedEdge> sp, int n) {
        List<double[]> rows = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            double[] r = new double[n];
            for (int j = 0; j < n; j++) {
                double x = i == j ? 0.0 : sp.getPathWeight(i, j);
                r[j] = Double.isInfinite(x) ? INF : x;
            }
            rows.add(r);
        }
        return rows;
    }
}
