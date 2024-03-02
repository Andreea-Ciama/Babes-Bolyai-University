package com.example.benchmark;

import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import com.example.*;

import java.util.List;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@Warmup(iterations = 10, time = 1)
@Measurement(iterations = 20, time = 1)
//@Fork(1)
@State(Scope.Benchmark)
public class DoubleObjectsRandomBenchmark {
    public static void main(String[] args) throws RunnerException {

        Options opt = new OptionsBuilder()
                .include(DoubleObjectsRandomBenchmark.class.getSimpleName())
                .forks(1)
                .build();

        new Runner(opt).run();
    }

    @Benchmark
    public Double testComputeSumRandom(MyState state) {
        return state.doubleObjectOperations.computeSum(state.randomOrder);
    }

    @Benchmark
    public Double testComputeAvgRandom(MyState state) {
        return state.doubleObjectOperations.computeAverage(state.randomOrder);
    }

    @Benchmark
    public void testTop10PercentBiggestNumbersRandom(MyState state) throws Exception {
        state.doubleObjectOperations.printTop10PercentBiggestNumbers(state.randomOrder);
    }

    @State(Scope.Thread)
    public static class MyState {
        DoubleObjectOperations doubleObjectOperations = new DoubleObjectOperations();
        List<Double> randomOrder;

        @Setup(Level.Trial)
        public void setUp() {
            randomOrder = doubleObjectOperations.generateRandomDoubleList(100_000_000);

        }
    }

}
