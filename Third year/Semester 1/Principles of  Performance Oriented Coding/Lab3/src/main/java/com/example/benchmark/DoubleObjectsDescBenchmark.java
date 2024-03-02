package com.example.benchmark;
import com.example.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

import java.util.Comparator;
import java.util.List;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@Warmup(iterations = 10, time = 1)
@Measurement(iterations = 20, time = 1)
//@Fork(1)
@State(Scope.Benchmark)
public class DoubleObjectsDescBenchmark {
    public static void main(String[] args) throws RunnerException {

        Options opt = new OptionsBuilder()
                .include(DoubleObjectsDescBenchmark.class.getSimpleName())
                .forks(1)
                .build();

        new Runner(opt).run();
    }

    @Benchmark
    public Double testComputeSumDesc(MyState state) {
        return state.doubleObjectOperations.computeSum(state.descOrder);
    }

    @Benchmark
    public Double testComputeAvgDesc(MyState state) {
        return state.doubleObjectOperations.computeAverage(state.descOrder);
    }

    @Benchmark
    public void testTop10PercentBiggestNumbersDesc(MyState state) throws Exception {
        state.doubleObjectOperations.printTop10PercentBiggestNumbers(state.descOrder);
    }

    @State(Scope.Thread)
    public static class MyState {
        DoubleObjectOperations doubleObjectOperations = new DoubleObjectOperations();
        List<Double> descOrder;

        @Setup(Level.Trial)
        public void setUp() {
            descOrder = doubleObjectOperations.generateRandomDoubleList(100_000_000);
            descOrder.sort(Comparator.reverseOrder());
        }
    }

}
