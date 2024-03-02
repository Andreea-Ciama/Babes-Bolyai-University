package com.example.benchmark;

import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import com.example.*;

import java.util.Arrays;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@Warmup(iterations = 10, time = 1)
@Measurement(iterations = 20, time = 1)
//@Fork(1)
@State(Scope.Benchmark)
public class DoublePrimitivesBenchmark {
    public static void main(String[] args) throws RunnerException {

        Options opt = new OptionsBuilder()
                .include(DoublePrimitivesBenchmark.class.getSimpleName())
                .forks(1)
                .build();

        new Runner(opt).run();
    }

    @Benchmark
    public double testComputeSumRandom(MyState state) {
        return state.doublePrimitiveOperations.computeSum(state.randomOrder);
    }

    @Benchmark
    public double testComputeSumAsc(MyState state) {
        return state.doublePrimitiveOperations.computeSum(state.ascOrder);
    }

    @Benchmark
    public double testComputeSumDesc(MyState state) {
        return state.doublePrimitiveOperations.computeSum(state.descOrder);
    }

    @Benchmark
    public double testComputeAvgRandom(MyState state) {
        return state.doublePrimitiveOperations.computeAverage(state.randomOrder);
    }

    @Benchmark
    public double testComputeAvgAsc(MyState state) {
        return state.doublePrimitiveOperations.computeAverage(state.ascOrder);
    }

    @Benchmark
    public double testComputeAvgDesc(MyState state) {
        return state.doublePrimitiveOperations.computeAverage(state.descOrder);
    }

    @Benchmark
    public void testTop10PercentBiggestNumbersRandom(MyState state) throws Exception {
        state.doublePrimitiveOperations.printTop10PercentBiggestNumbers(state.randomOrder);
    }

    @Benchmark
    public void testTop10PercentBiggestNumbersAsc(MyState state) throws Exception {
        state.doublePrimitiveOperations.printTop10PercentBiggestNumbers(state.ascOrder);
    }

    @Benchmark
    public void testTop10PercentBiggestNumbersDesc(MyState state) throws Exception {
        state.doublePrimitiveOperations.printTop10PercentBiggestNumbers(state.descOrder);
    }

    @State(Scope.Thread)
    public static class MyState {
        DoublePrimitiveOperations doublePrimitiveOperations = new DoublePrimitiveOperations();

        double[] randomOrder;
        double[] ascOrder;
        double[] descOrder;

        @Setup(Level.Trial)
        public void setUp() {
            randomOrder = doublePrimitiveOperations.generateRandomDoubleList(100_000_000);
            ascOrder = doublePrimitiveOperations.generateRandomDoubleList(100_000_000);
            descOrder = doublePrimitiveOperations.generateRandomDoubleList(100_000_000);

            Arrays.sort(ascOrder);
            Arrays.sort(descOrder);
            // Reverse the sorted array to get descending order, so we don't have to convert it to Double
            // to use collection function (which use only objects -> Double)
            for (int i = 0; i < descOrder.length / 2; i++) {
                double aux = descOrder[i];
                descOrder[i] = descOrder[descOrder.length - i - 1];
                descOrder[descOrder.length - i - 1] = aux;
            }
        }
    }

}
