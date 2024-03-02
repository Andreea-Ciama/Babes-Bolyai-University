

package org.example;

import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.Blackhole;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Measurement(iterations = 10, batchSize = 100000)
@Warmup(iterations = 10, batchSize = 10000)
@Fork(1)
public class MyBenchmark {
    @org.openjdk.jmh.annotations.State(Scope.Thread)
    public static class State {
        public DoublePrimitiveCalculator data = new DoublePrimitiveCalculator();
        @Setup(Level.Invocation)
        public void setup() {
            List<Double> numbers = new ArrayList<>();
            for (int i = 0; i < 100000; i++)
                numbers.add(ThreadLocalRandom.current().nextDouble());
            // numbers.add((double) i);

            data.populate(numbers);
        }
    }

    @Benchmark
    public void testAdd(State state, Blackhole blackhole) {
        blackhole.consume(state.data.sum());
    }
    @Benchmark
    public void testAverage(State state, Blackhole blackhole) {
        blackhole.consume(state.data.average());
    }
    @Benchmark
    public void testTop(State state, Blackhole blackhole) {
        blackhole.consume(state.data.top10percent());
    }

}
