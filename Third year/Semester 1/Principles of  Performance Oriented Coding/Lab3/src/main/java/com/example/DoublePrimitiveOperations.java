package com.example;

import org.apache.commons.io.output.NullOutputStream;

import java.io.PrintStream;
import java.util.Arrays;
import java.util.Random;

public class DoublePrimitiveOperations {
    public double[] generateRandomDoubleList(int size) {
        double[] generatedDoubles = new double[size];
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            generatedDoubles[i] = random.nextDouble();
        }
        return generatedDoubles;
    }

    public double computeSum(double[] doubles) {
        return Arrays.stream(doubles).sum();
    }

    public double computeAverage(double[] doubles) {
        double sum = computeSum(doubles);
        return sum / doubles.length;
    }

    public void printTop10PercentBiggestNumbers(double[] doubles) throws Exception {
        int size = doubles.length;

        if (size / 10 < 1) {
            throw new Exception("List is too small to find top 10% elements.");
        }

        PrintStream nullOutput = new PrintStream(NullOutputStream.INSTANCE);
        PrintStream oldOutput = System.out;

        // Redirect System.out to nullOutput
        System.setOut(nullOutput);

        Arrays.stream(doubles)
                .sorted()
                .skip(doubles.length - size / 10)
                .forEach(System.out::println);

        System.setOut(oldOutput);
        nullOutput.close();
    }
}
