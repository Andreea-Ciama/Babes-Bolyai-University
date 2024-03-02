package org.example;

import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class BigDecimalCalculator {
    List<BigDecimal> data = new ArrayList<BigDecimal>();

    public void populate(Iterable<BigDecimal> source) {
        data = new ArrayList<>();
        for (BigDecimal element : source)
            data.add(element);
    }

    BigDecimal sum() {
        return this.data.stream().reduce(new BigDecimal(0), BigDecimal::add);
    }

    BigDecimal average() {
        return this.sum().divide(new BigDecimal(this.data.size()), MathContext.DECIMAL128);
    }

    List<BigDecimal> top10percent() {
        return this
                .data
                .stream()
                .sorted(Comparator.reverseOrder())
                .limit(this.data.size() / 10)
                .collect(Collectors.toList());
    }
}
