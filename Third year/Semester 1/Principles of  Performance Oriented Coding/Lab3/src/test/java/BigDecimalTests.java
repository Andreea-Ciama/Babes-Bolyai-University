import com.example.BigDecimalOperations;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.math.BigDecimal;
import java.util.Arrays;
import java.util.List;

public class BigDecimalTests {

    BigDecimalOperations bigDecimalOperations; // The class that is going to be tested

    @BeforeEach
    void setUp() {
        bigDecimalOperations = new BigDecimalOperations(); // using default not declared constructor provided by Java
    }

    @Test
    void generateRandomBigDecimalList() {
        int size = 100;
        List<BigDecimal> generatedBigDecimals = bigDecimalOperations.generateRandomBigDecimalList(size);
        Assertions.assertEquals(size, generatedBigDecimals.size());
        for (BigDecimal bd : generatedBigDecimals) {
            Assertions.assertNotNull(bd);
        }
    }

    @Test
    void computeSum() {
        List<BigDecimal> bigDecimals = Arrays.asList(new BigDecimal("10.42"),
                new BigDecimal("31.4"),
                new BigDecimal("5.39"));
        BigDecimal expectedSum = new BigDecimal("47.21");
        BigDecimal actualSum = bigDecimalOperations.computeSum(bigDecimals);
        Assertions.assertEquals(expectedSum, actualSum);
    }

    @Test
    void computeAverage() {
        List<BigDecimal> bigDecimals = Arrays.asList(new BigDecimal("10.42"),
                new BigDecimal("31.4"),
                new BigDecimal("5.39"));
        BigDecimal expectedAvg = new BigDecimal("15.74");
        BigDecimal actualAvg = bigDecimalOperations.computeAverage(bigDecimals);
        Assertions.assertEquals(expectedAvg, actualAvg);
    }

    @Test
    void printTop10PercentBiggestNumbers() {
        List<BigDecimal> bigDecimals = Arrays.asList(new BigDecimal("12.5"),
                new BigDecimal("17.3"),
                new BigDecimal("8.9"),
                new BigDecimal("25.1"),
                new BigDecimal("19.7"),
                new BigDecimal("11.0"),
                new BigDecimal("15.8"),
                new BigDecimal("22.6"),
                new BigDecimal("14.3"),
                new BigDecimal("10.2"),
                new BigDecimal("16.5"));

        // Capture the printed output by redirecting output for testing purposes.
        StringBuffer buffer = new StringBuffer();
        System.setOut(new PrintStream(new ByteArrayOutputStream() { // anonymous class
            public void write(byte[] b, int off, int len) { // overrides the 'write' method
                buffer.append(new String(b, off, len));
            }
        }));

        try {
            bigDecimalOperations.printTop10PercentBiggestNumbers(bigDecimals);
        } catch (Exception ignored) {
        }

        // Get the printed output
        String output = buffer.toString();

        // Assert the output contains the expected numbers
        // Assertions.assertEquals(1, output.length());
        Assertions.assertTrue(output.contains("25.1"));

        List<BigDecimal> bigDecimalsWrong = Arrays.asList(new BigDecimal("12.5"),
                new BigDecimal("17.3"),
                new BigDecimal("8.9"));
        var thrown = Assertions.assertThrows(Exception.class,
                () -> bigDecimalOperations.printTop10PercentBiggestNumbers(bigDecimalsWrong));
        Assertions.assertEquals("List is too small to find top 10% elements.", thrown.getMessage());

    }
}
