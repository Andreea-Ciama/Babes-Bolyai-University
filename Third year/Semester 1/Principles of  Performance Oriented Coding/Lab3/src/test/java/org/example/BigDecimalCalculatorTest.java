package org.example;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class BigDecimalCalculatorTest {
    private BigDecimalCalculator calculator;

    @BeforeEach
    void setUp() {
        calculator = new BigDecimalCalculator();
        calculator.populate(Arrays.asList(
                new BigDecimal(1),
                new BigDecimal(2),
                new BigDecimal(3),
                new BigDecimal(4),
                new BigDecimal(5),
                new BigDecimal(6),
                new BigDecimal(7),
                new BigDecimal(8),
                new BigDecimal(9),
                new BigDecimal(10)
        ));
    }

    @Test
    void sum() {
        assertEquals(this.calculator.sum(), new BigDecimal(55));
    }

    @Test
    void average() {
        assertEquals(this.calculator.average(), new BigDecimal("5.5"));
    }

    @Test
    void top10percent() {
        List<BigDecimal> result = this.calculator.top10percent();
        assertEquals(result.size(), 1);
        assertEquals(result.get(0), new BigDecimal(10));
    }
}