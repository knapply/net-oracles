import java.nio.file.*;
import java.util.*;
import org.gephi.graph.api.GraphModel;
import org.gephi.statistics.plugin.Modularity;

/**
 * Child process of Oracle.java for the Louvain entries: runs the toolkit's
 * Modularity statistic repeatedly on the main thread of a fresh JVM and prints
 * "R index value" per run.
 *
 * Why a fresh JVM and the main thread: with setRandom(false) the statistic still
 * depends on the iteration order of hashed collections, which follows the
 * identity hash codes of the objects it creates. HotSpot derives those from a
 * per-thread generator, so the result of a run depends on which thread runs it
 * and on what that thread did before. On the main thread of a fresh JVM the
 * whole sequence of runs is the same every time (checked across JVMs and CPU
 * counts); on pooled worker threads, or after unrelated work, it is not.
 *
 * Runs listed in the exclusion argument (those that did not return in an
 * earlier attempt) go to a throwaway thread with a time limit and are left out,
 * so they cannot disturb the main thread's sequence.
 *
 * Arguments: fixture directory, w|u (weighted or not), number of runs,
 * comma-separated indices of excluded runs (or -).
 */
public class Louvain20 {
    static double one(Oracle.Fx f, boolean useW) {
        GraphModel gm = Oracle.build(f, useW);
        Modularity m = new Modularity();
        m.setRandom(false);
        m.setUseWeight(useW);
        m.setResolution(1.0);
        m.execute(gm);
        return m.getModularity();
    }

    public static void main(String[] a) throws Exception {
        Oracle.errors = new java.io.PrintWriter(System.err, true);
        Oracle.Fx f = Oracle.load(Paths.get(a[0]));
        boolean useW = a[1].equals("w");
        int runs = Integer.parseInt(a[2]);
        Set<Integer> skip = new HashSet<>();
        if (!a[3].equals("-")) for (String s : a[3].split(",")) skip.add(Integer.parseInt(s));
        for (int i = 0; i < runs; i++) {
            if (skip.contains(i)) {
                final double[] box = {Double.NaN};
                Thread t = new Thread(() -> { box[0] = one(f, useW); });
                t.setDaemon(true); t.start(); t.join(10000);
                continue;
            }
            System.out.println("R " + i + " " + Double.toString(one(f, useW)));
            System.out.flush();
        }
        System.out.println("DONE");
        System.out.flush();
        System.exit(0);
    }
}
