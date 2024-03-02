package com.example.benchmark;

import com.example.BigDecimalOperations.*;
import com.example.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@Warmup(iterations = 10, time = 1)
@Measurement(iterations = 20, time = 1)
//@Fork(1)
@State(Scope.Benchmark)
public class DoubleObjectsAscBenchmark {
    public static void main(String[] args) throws RunnerException {

        Options opt = new OptionsBuilder()
                .include(DoubleObjectsAscBenchmark.class.getSimpleName())
                .forks(1)
                .build();

        new Runner(opt).run();
    }

    @Benchmark
    public Double testComputeSumAsc(MyState state) {
        return state.doubleObjectOperations.computeSum(state.ascOrder);
    }

    @Benchmark
    public Double testComputeAvgAsc(MyState state) {
        return state.doubleObjectOperations.computeAverage(state.ascOrder);
    }

    @Benchmark
    public void testTop10PercentBiggestNumbersAsc(MyState state) throws Exception {
        state.doubleObjectOperations.printTop10PercentBiggestNumbers(state.ascOrder);
    }

    @State(Scope.Thread)
    public static class MyState {
        DoubleObjectOperations doubleObjectOperations = new DoubleObjectOperations();
        List<Double> ascOrder;

        @Setup(Level.Trial)
        public void setUp() {
            ascOrder = doubleObjectOperations.generateRandomDoubleList(100_000_000);
            Collections.sort(ascOrder);
        }
    }
}
