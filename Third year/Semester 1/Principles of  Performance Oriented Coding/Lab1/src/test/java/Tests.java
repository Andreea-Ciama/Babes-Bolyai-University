import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Tests {

        @Test
        public void testAdd() {
            Calculator calculator = new Calculator();
            assertEquals(5.0, calculator.add(2.0, 3.0), 0.0001);
        }

        @Test
        public void testSubtract() {
            Calculator calculator = new Calculator();
            assertEquals(2.0, calculator.subtract(5.0, 3.0), 0.0001);
        }

        @Test
        public void testMultiply() {
            Calculator calculator = new Calculator();
            assertEquals(15.0, calculator.multiply(3.0, 5.0), 0.0001);
        }

        @Test
        public void testDivide() {
            Calculator calculator = new Calculator();
            assertEquals(2.0, calculator.divide(6.0, 3.0), 0.0001);
        }
        @Test
        public void testDivideByZero() {
            Calculator calculator = new Calculator();
            assertThrows(ArithmeticException.class, () -> calculator.divide(5.0, 0.0));
        }

    @Test
        public void testMin() {
            Calculator calculator = new Calculator();
        assertEquals(3.0, calculator.min(3.0, 5.0), 0.0001);
       }

        @Test
        public void testMax() {
            Calculator calculator = new Calculator();
            assertEquals(5.0, calculator.max(3.0, 5.0), 0.0001);
        }

        @Test
        public void testSqrt() {
            Calculator calculator = new Calculator();
            assertEquals(2.0, calculator.sqrt(4.0), 0.0001);
        }

        @Test
        public void testSqrtOfNegativeNumber() {
            Calculator calculator = new Calculator();
            assertThrows(ArithmeticException.class, () -> calculator.sqrt(-4.0));
        }

}
