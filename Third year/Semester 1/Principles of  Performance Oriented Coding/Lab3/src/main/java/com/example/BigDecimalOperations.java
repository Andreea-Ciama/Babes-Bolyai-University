package com.example;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Random;

public class BigDecimalOperations {

    public List<BigDecimal> generateRandomBigDecimalList(int size) {
        List<BigDecimal> generatedBigDecimals = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            BigDecimal randomBigDecimal = BigDecimal.valueOf(random.nextDouble());
            generatedBigDecimals.add(randomBigDecimal);
        }
        return generatedBigDecimals;
    }

    public BigDecimal computeSum(List<BigDecimal> bigDecimals) {
        return bigDecimals.stream().reduce(BigDecimal.ZERO, BigDecimal::add);
    }

    public BigDecimal computeAverage(List<BigDecimal> bigDecimals) {
        BigDecimal sum = computeSum(bigDecimals);
        return sum.divide(new BigDecimal(bigDecimals.size()), 2, RoundingMode.HALF_UP); // scale=2 -> 2 decimals
    }

    public void printTop10PercentBiggestNumbers(List<BigDecimal> bigDecimals) throws Exception {
        // 10/100 * size = ? how many numbers represent that 10% of the list => numbers = size/10;
        int size = bigDecimals.size();

        if (size / 10 < 1) {
            throw new Exception("List is too small to find top 10% elements.");
        }
        bigDecimals.stream()
                .sorted(Comparator.reverseOrder()) // sort in descending order
                .limit(size / 10) // int/int = int by convention
                .forEach(System.out::println);
    }

}
