package com.jenkov;

import java.util.concurrent.TimeUnit;

import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import Other.Order;
import Repository.*;


public class Tests {
    private static final Order order = new Order(2, 3, 5);
    @State(Scope.Benchmark)
    @BenchmarkMode(Mode.AverageTime)
    @OutputTimeUnit(TimeUnit.NANOSECONDS)
    @Fork(1)

    public static class ArrayListBasedRepositoryBenchmark {
        ArrayListBasedRepository<Order> arrayListBasedRepository = new ArrayListBasedRepository<>();
    }

    @Benchmark
    public void add_arrayListBasedRepository(ArrayListBasedRepositoryBenchmark state) {
        state.arrayListBasedRepository.add(order);
    }

     @Benchmark
     public void contains_arrayListBasedRepository( ArrayListBasedRepositoryBenchmark  state) {
         state.arrayListBasedRepository.contains(order);
     }

     @Benchmark
     public void remove_arrayListBasedRepository( ArrayListBasedRepositoryBenchmark  state) {
         state.arrayListBasedRepository.remove(order);
     }

    @State(Scope.Benchmark)
    public static class ConcurrentHashMapBasedRepositoryBenchmark {
        Repository.ConcurrentHashMapBasedRepository<Integer, Other.Order> concurrentHashMapBasedRepository = new Repository.ConcurrentHashMapBasedRepository<>();
    }

    @Benchmark
    public void add_concurrentHashMapBasedRepository(ConcurrentHashMapBasedRepositoryBenchmark state) {
        state.concurrentHashMapBasedRepository.add(1, order);
    }

    @Benchmark
    public void contains_concurrentHashMapBasedRepository(ConcurrentHashMapBasedRepositoryBenchmark state) {
        state.concurrentHashMapBasedRepository.contains(order);
    }

    @Benchmark
    public void remove_concurrentHashMapBasedRepository(ConcurrentHashMapBasedRepositoryBenchmark state) {
        state.concurrentHashMapBasedRepository.remove(order);
    }


    @State(Scope.Benchmark)
    public static class FastUtilBasedRepositoryBenchmark {
        Repository.FastUtilBasedRepository fastUtilBasedRepository = new Repository.FastUtilBasedRepository();
    }

    @Benchmark
    public void add_fastUtilBasedRepository(FastUtilBasedRepositoryBenchmark state) {
        state.fastUtilBasedRepository.add(1.2, 4.6);
    }

    @Benchmark
    public void contains_fastUtilBasedRepository(FastUtilBasedRepositoryBenchmark state) {
        state.fastUtilBasedRepository.contains(4.6);
    }

    @Benchmark
    public void remove_fastUtilBasedRepository(FastUtilBasedRepositoryBenchmark state) {
        state.fastUtilBasedRepository.remove(4.6);
    }


    @State(Scope.Benchmark)
    public static class HashBagBasedRepositoryBenchmark {
        Repository.HashBagBasedRepository<Other.Order> hashBagBasedRepository = new Repository.HashBagBasedRepository<>();
    }

    @Benchmark
    public void add_hashBagBasedRepository(HashBagBasedRepositoryBenchmark state) {
        state.hashBagBasedRepository.add(order);
    }

    @Benchmark
    public void contains_hashBagBasedRepository(HashBagBasedRepositoryBenchmark state) {
        state.hashBagBasedRepository.contains(order);
    }

    @Benchmark
    public void remove_hashBagBasedRepository(HashBagBasedRepositoryBenchmark state) {
        state.hashBagBasedRepository.remove(order);
    }

    @State(Scope.Benchmark)
    public static class HashSetBasedRepositoryBenchmark {
        Repository.HashSetBasedRepository<Other.Order> hashSetBasedRepository = new Repository.HashSetBasedRepository<>();
    }

    @Benchmark
    public void add_hashSetBasedRepository(HashSetBasedRepositoryBenchmark state) {
        state.hashSetBasedRepository.add(order);
    }

    @Benchmark
    public void contains_hashSetBasedRepository(HashSetBasedRepositoryBenchmark state) {
        state.hashSetBasedRepository.contains(order);
    }

    @Benchmark
    public void remove_hashSetBasedRepository(HashSetBasedRepositoryBenchmark state) {
        state.hashSetBasedRepository.remove(order);
    }


    @State(Scope.Benchmark)
    public static class TreeSetBasedRepositoryBenchmark {
        Repository.TreeSetBasedRepository<Other.Order> treeSetBasedRepository = new Repository.TreeSetBasedRepository<>();
    }

    @Benchmark
    public void add_treeSetBasedRepository(TreeSetBasedRepositoryBenchmark state) {
        state.treeSetBasedRepository.add(order);
    }

    @Benchmark
    public void contains_treeSetBasedRepository(TreeSetBasedRepositoryBenchmark state) {
        state.treeSetBasedRepository.contains(order);
    }

    @Benchmark
    public void remove_treeSetBasedRepository(TreeSetBasedRepositoryBenchmark state) {
        state.treeSetBasedRepository.remove(order);
    }


    public static void main(String[] args) throws Exception {
        System.setProperty("https.protocols", "TLSv1");
        Options opt = new OptionsBuilder()
                  .include(Tests.class.getSimpleName())
                   // .addProfiler(.class)
                    .forks(1)
                  .build();

          new Runner(opt).run();
         //org.openjdk.jmh.Main.main(args);
     }

}