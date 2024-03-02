package com.example;

import org.apache.commons.io.output.NullOutputStream;

import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Random;

public class DoubleObjectOperations {
    public List<Double> generateRandomDoubleList(int size) {
        List<Double> generatedDoubles = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            Double randomDouble = random.nextDouble();
            generatedDoubles.add(randomDouble);
        }
        return generatedDoubles;
    }

    public Double computeSum(List<Double> doubles) {
        return doubles.stream().reduce(0.0, Double::sum);
    }

    public Double computeAverage(List<Double> doubles) {
        Double sum = computeSum(doubles);
        return sum / doubles.size();
    }

    public void printTop10PercentBiggestNumbers(List<Double> doubles) throws Exception {
        int size = doubles.size();

        if (size / 10 < 1) {
            throw new Exception("List is too small to find top 10% elements.");
        }

        PrintStream nullOutput = new PrintStream(NullOutputStream.INSTANCE);
        PrintStream oldOut = System.out;

        // Redirect System.out to nullOutput
        System.setOut(nullOutput);

        doubles.stream()
                .sorted(Comparator.reverseOrder())
                .limit(size / 10)
                .forEach(System.out::println);

        System.setOut(oldOut);
        nullOutput.close();
    }
}
