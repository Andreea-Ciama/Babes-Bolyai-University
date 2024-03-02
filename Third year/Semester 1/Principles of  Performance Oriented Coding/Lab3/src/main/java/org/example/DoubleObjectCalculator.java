package org.example;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class DoubleObjectCalculator {
    List<Double> data = new ArrayList<>();

    public void populate(Iterable<Double> source) {
        data = new ArrayList<>();
        for (Double element : source)
            data.add(element);
    }

    Double sum() {
        return this.data.stream().reduce(0.0d, Double::sum);
    }

    Double average() {
        return this.sum() / this.data.size();
    }

    List<Double> top10percent() {
        return this
                .data
                .stream()
                .sorted(Comparator.reverseOrder())
                .limit(this.data.size() / 10)
                .collect(Collectors.toList());
    }
}
