// Gephi toolkit oracle driver: reads the fixture corpus and writes golden files.
// Black-box use of the published jar and its public API only.  Usage:
//   java -Djava.awt.headless=true -cp <jar>:. Oracle <fixtures_dir> <out_dir>
import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.regex.*;
import org.gephi.graph.api.Configuration;
import org.gephi.graph.api.Edge;
import org.gephi.graph.api.Graph;
import org.gephi.graph.api.GraphModel;
import org.gephi.graph.api.Node;
import org.gephi.statistics.plugin.*;

public class Oracle {
    static final double NAN = -999.0, INF = -1000.0;   // descriptive / core markers
    static Path out;
    static PrintWriter errors;

    static class Fx {
        String name; int n; boolean directed, weighted; int m;
        int[] src, tgt; double[] w; Path dir;
    }

    static Fx load(Path dir) throws IOException {
        Fx f = new Fx(); f.name = dir.getFileName().toString(); f.dir = dir;
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

    // The network as given: loops and parallel edges are kept (parallel edges
    // of the same type are enabled in the graph store); weights are 1 unless useW.
    static GraphModel build(Fx f, boolean useW) {
        Configuration cfg = Configuration.builder().enableParallelEdgesSameType(true).build();
        GraphModel gm = GraphModel.Factory.newInstance(cfg);
        Graph g = gm.getGraph();
        Node[] nd = new Node[f.n];
        for (int v = 0; v < f.n; v++) { nd[v] = gm.factory().newNode(Integer.toString(v)); g.addNode(nd[v]); }
        int added = 0;
        for (int i = 0; i < f.m; i++) {
            Edge e = gm.factory().newEdge(nd[f.src[i]], nd[f.tgt[i]], 0, useW ? f.w[i] : 1.0, f.directed);
            if (g.addEdge(e)) added++;
        }
        if (added != f.m) errors.println(f.name + "\tbuild\tstored " + added + " of " + f.m + " edges");
        return gm;
    }

    static double attr(Node v, String col) {
        Object o = v.getAttribute(col);
        return o == null ? Double.NaN : ((Number) o).doubleValue();
    }
    static double[] column(GraphModel gm, int n, String col) {
        double[] r = new double[n];
        Arrays.fill(r, Double.NaN);
        for (Node v : gm.getGraph().getNodes()) r[Integer.parseInt((String) v.getId())] = attr(v, col);
        return r;
    }
    static double mark(double x, double nan, double inf) { return Double.isNaN(x) ? nan : Double.isInfinite(x) ? inf : x; }
    static double[] marked(double[] x, double nan, double inf) {
        double[] r = new double[x.length];
        for (int i = 0; i < x.length; i++) r[i] = mark(x[i], nan, inf);
        return r;
    }

    static String fmt(double x) { return Double.isNaN(x) ? "NaN" : Double.toString(x); }

    static void put(Fx f, String variant, double[] vals) throws IOException {
        Path d = out.resolve(f.name); Files.createDirectories(d);
        try (PrintWriter pw = new PrintWriter(d.resolve(variant + ".csv").toFile())) {
            pw.print("value\n");
            for (double x : vals) pw.print(fmt(x) + "\n");
        }
    }
    static void put1(Fx f, String variant, double v) throws IOException { put(f, variant, new double[] {v}); }

    interface Job { void run() throws Exception; }
    // Each job runs in a worker thread with a time limit, so that a run of the
    // toolkit that does not return is recorded and skipped (see ERRORS.tsv).
    static final java.util.concurrent.ExecutorService POOL = java.util.concurrent.Executors.newCachedThreadPool(r -> {
        Thread t = new Thread(r); t.setDaemon(true); return t;
    });
    static void tryRun(Fx f, String variant, Job j) {
        java.util.concurrent.Future<?> fut = POOL.submit(() -> { j.run(); return null; });
        try { fut.get(300, java.util.concurrent.TimeUnit.SECONDS); }
        catch (java.util.concurrent.TimeoutException t) {
            fut.cancel(true);
            errors.println(f.name + "\t" + variant + "\ttimeout after 300 s");
        }
        catch (java.util.concurrent.ExecutionException e) {
            Throwable t = e.getCause();
            errors.println(f.name + "\t" + variant + "\t" + t.getClass().getSimpleName() + ": "
                + String.valueOf(t.getMessage()).replace('\n', ' '));
        }
        catch (InterruptedException e) { throw new RuntimeException(e); }
        errors.flush();
    }

    // The 20 Louvain runs of one entry, in child JVMs running Louvain20 (see there for
    // why). Returns the values of the runs that returned; a run that does not return
    // within 30 s is logged and left out, and the child is restarted with that run
    // excluded, so the other runs keep the values they had.
    static double[] louvainRuns(Fx f, String name, boolean useW, int runs) throws Exception {
        TreeSet<Integer> skip = new TreeSet<>();
        for (int attempt = 0; attempt <= 5; attempt++) {
            String sk = skip.isEmpty() ? "-" : skip.toString().replaceAll("[\\[\\] ]", "");
            Process pr = new ProcessBuilder(Paths.get(System.getProperty("java.home"), "bin", "java").toString(),
                "-Djava.awt.headless=true", "-cp", System.getProperty("java.class.path"), "Louvain20",
                f.dir.toString(), useW ? "w" : "u", Integer.toString(runs), sk)
                .redirectError(ProcessBuilder.Redirect.DISCARD).start();
            java.util.concurrent.BlockingQueue<String> q = new java.util.concurrent.LinkedBlockingQueue<>();
            Thread rd = new Thread(() -> {
                try (BufferedReader br = new BufferedReader(new InputStreamReader(pr.getInputStream()))) {
                    String l; while ((l = br.readLine()) != null) q.add(l);
                } catch (IOException e) { /* process killed */ }
                q.add("EOF");
            });
            rd.setDaemon(true); rd.start();
            List<Double> vals = new ArrayList<>();
            int hung = -1;
            while (true) {
                String l = q.poll(30, java.util.concurrent.TimeUnit.SECONDS);
                if (l == null) {
                    // the next run that has not been reported
                    hung = nextUnreported(skip, vals.size(), runs);
                    break;
                }
                if (l.equals("DONE")) break;
                if (l.equals("EOF")) throw new RuntimeException("Louvain20 exited early");
                vals.add(Double.parseDouble(l.split(" ")[2]));
            }
            pr.destroyForcibly();
            if (hung < 0) {
                double[] r = new double[vals.size()];
                for (int i = 0; i < r.length; i++) r[i] = vals.get(i);
                return r;
            }
            errors.println(f.name + "\t" + name + "\trun " + hung + " did not finish in 30 s");
            skip.add(hung);
        }
        throw new RuntimeException("too many runs that did not return");
    }
    // Index of the first run that is neither excluded nor reported, given that
    // `reported` runs have been printed.
    static int nextUnreported(Set<Integer> skip, int reported, int runs) {
        int i = 0, seen = 0;
        while (i < runs) {
            if (!skip.contains(i)) { if (seen == reported) return i; seen++; }
            i++;
        }
        return runs - 1;
    }

    static void process(Fx f) {
        final int n = f.n;
        final boolean dir = f.directed;
        // Degree: counts of stored edges.
        tryRun(f, "degree", () -> {
            GraphModel gm = build(f, false);
            new Degree().execute(gm);
            put(f, "degree_all", column(gm, n, Degree.DEGREE));
            if (dir) {
                put(f, "degree_in", column(gm, n, Degree.INDEGREE));
                put(f, "degree_out", column(gm, n, Degree.OUTDEGREE));
            }
        });
        if (f.weighted) tryRun(f, "strength", () -> {
            GraphModel gm = build(f, true);
            new WeightedDegree().execute(gm);
            put(f, "strength_all", column(gm, n, WeightedDegree.WDEGREE));
        });
        // Graph distance (hop counts; the statistic has no weighted mode), as the
        // network is stored and, for directed networks, with directions ignored.
        for (int mode = 0; mode < 2; mode++) {
            final int md = mode;
            final boolean asDirected = mode == 0 && dir;
            if (mode == 1 && !dir) break;
            for (int norm = 0; norm < 2; norm++) {
                final boolean normalized = norm == 1;
                final String nt = normalized ? "_normalized" : "";
                tryRun(f, "graph_distance_" + mode + nt, () -> {
                    GraphModel gm = build(f, false);
                    GraphDistance gd = new GraphDistance();
                    gd.setDirected(asDirected);
                    gd.setNormalized(normalized);
                    gd.execute(gm);
                    double[] bt = column(gm, n, GraphDistance.BETWEENNESS);
                    double[] cl = marked(column(gm, n, GraphDistance.CLOSENESS), -1, -1);
                    double[] hc = marked(column(gm, n, GraphDistance.HARMONIC_CLOSENESS), -1, -1);
                    double[] ec = marked(column(gm, n, GraphDistance.ECCENTRICITY), NAN, INF);
                    // Closeness and harmonic closeness do not depend on setNormalized (checked on
                    // every fixture); they are written once, from the normalized run.
                    if (md == 0) {
                        put(f, "betweenness" + nt, bt);
                        if (normalized) {
                            put(f, "closeness_normalized", cl);
                            put(f, "harmonic_normalized", hc);
                        }
                        if (!normalized) {
                            put1(f, "diameter", mark(gd.getDiameter(), NAN, INF));
                            put1(f, "mean_distance", mark(gd.getPathLength(), NAN, INF));
                            put(f, dir ? "eccentricity_out" : "eccentricity", ec);
                            if (!dir) put1(f, "radius", mark(gd.getRadius(), NAN, INF));
                        }
                    } else {
                        if (normalized) put(f, "closeness_all", cl);
                        else {
                            put(f, "eccentricity", ec);
                            put1(f, "radius", mark(gd.getRadius(), NAN, INF));
                            put1(f, "diameter_all", mark(gd.getDiameter(), NAN, INF));
                            put1(f, "mean_distance_all", mark(gd.getPathLength(), NAN, INF));
                        }
                    }
                });
            }
        }
        // Eigenvector centrality (power iteration with a fixed number of runs).
        for (int mode = 0; mode < 2; mode++) {
            final boolean asDirected = mode == 0 && dir;
            if (mode == 1 && !dir) break;
            for (int wt = 0; wt < 2; wt++) {
                if (wt == 1 && (!f.weighted || mode == 1)) continue;
                final boolean useW = wt == 1;
                final String name = useW ? "eigenvector_weighted" : mode == 0 ? "eigenvector" : "eigenvector_undirected";
                tryRun(f, name, () -> {
                    GraphModel gm = build(f, useW);
                    EigenvectorCentrality ec = new EigenvectorCentrality();
                    ec.setDirected(asDirected);
                    ec.setNumRuns(1000000);
                    ec.execute(gm);
                    put(f, name, marked(column(gm, n, EigenvectorCentrality.EIGENVECTOR), -1, -1));
                });
            }
        }
        // PageRank, damping 0.85, tight tolerance.
        for (int mode = 0; mode < 2; mode++) {
            final boolean asDirected = mode == 0 && dir;
            if (mode == 1 && !dir) break;
            for (int wt = 0; wt < 2; wt++) {
                if (wt == 1 && (!f.weighted || mode == 1)) continue;
                final boolean useW = wt == 1;
                final String name = useW ? "pagerank_weighted" : mode == 0 ? "pagerank" : "pagerank_undirected";
                tryRun(f, name, () -> {
                    GraphModel gm = build(f, useW);
                    PageRank pr = new PageRank();
                    pr.setDirected(asDirected);
                    pr.setProbability(0.85);
                    pr.setEpsilon(1e-14);
                    pr.setUseEdgeWeight(useW);
                    pr.execute(gm);
                    put(f, name, column(gm, n, PageRank.PAGERANK));
                });
            }
        }
        // HITS.
        tryRun(f, "hits", () -> {
            GraphModel gm = build(f, false);
            Hits h = new Hits();
            h.setUndirected(!dir);
            h.setEpsilon(1e-14);
            h.execute(gm);
            put(f, "hits_authorities", column(gm, n, Hits.AUTHORITY));
            put(f, "hits_hubs", column(gm, n, Hits.HUB));
        });
        // Clustering coefficient and triangles, directions ignored.
        tryRun(f, "clustering", () -> {
            GraphModel gm = build(f, false);
            ClusteringCoefficient cc = new ClusteringCoefficient();
            cc.setDirected(false);
            cc.execute(gm);
            double[] c = column(gm, n, ClusteringCoefficient.CLUSTERING_COEFF);
            put(f, "clustering_zero", marked(c, NAN, INF));
            put1(f, "average_clustering", mark(cc.getAverageClusteringCoefficient(), NAN, INF));
            if (!dir) {
                // The triangle counts come in an internal order (nodes by decreasing degree),
                // so only their multiset is comparable with node-aligned values.
                double[] t = cc.getTriangesReuslts().clone();
                Arrays.sort(t);
                put(f, "nxo_triangles_sorted", t);
            }
        });
        // Connected components.
        tryRun(f, "components", () -> {
            GraphModel gm = build(f, false);
            ConnectedComponents cc = new ConnectedComponents();
            cc.setDirected(dir);
            cc.execute(gm);
            put(f, "components_weak", column(gm, n, ConnectedComponents.WEAKLY));
            if (dir) put(f, "components_strong", column(gm, n, ConnectedComponents.STRONG));
            else put(f, "components_strong", column(gm, n, ConnectedComponents.WEAKLY));
        });
        // Density (the statistic's own directed flag).
        tryRun(f, "density", () -> {
            GraphModel gm = build(f, false);
            GraphDensity gd = new GraphDensity();
            gd.setDirected(dir);
            gd.execute(gm);
            put1(f, "density", mark(gd.getDensity(), -1, -1));
        });
        // Louvain modularity: resolution 1, no randomization. Repeated runs of the
        // statistic differ (see docs/drafts/correctness_findings.md), so the golden
        // value is the mean over 20 fresh runs, like the other tools' entries.
        if (!dir) for (int v = 0; v < 2; v++) {
            final boolean useW = v == 1;
            if (useW && !f.weighted) continue;
            final String name = useW ? "louvain_quality_weighted" : "louvain_quality";
            tryRun(f, name, () -> {
                // Mean over 20 runs on the main thread of a fresh JVM (see Louvain20).
                double[] r = louvainRuns(f, name, useW, 20);
                if (r.length < 10) throw new RuntimeException("only " + r.length + " of 20 runs finished");
                double sum = 0; for (double x : r) sum += x;
                put1(f, name, sum / r.length);
            });
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
        for (Path d : dirs) { System.err.println("fixture " + d.getFileName()); process(load(d)); }
        errors.close();
        System.exit(0);   // the toolkit may leave non-daemon threads running
    }
}
