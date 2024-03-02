import java.util.Scanner;


public class CommandLineCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Calculator calculator = new Calculator();

        while (true) {
            System.out.println("Enter operation (+, -, *, /, min, max, sqrt) or 'exit' to quit: ");
            String operation = scanner.next();

            if (operation.equals("exit")) {
                break;
            }

            double result;

            if (operation.equals("+") || operation.equals("-") || operation.equals("*") || operation.equals("/") || operation.equals("min") || operation.equals("max")) {
                System.out.println("Enter two numbers: ");
                double num1 = scanner.nextDouble();
                double num2 = scanner.nextDouble();

                result = switch (operation) {
                    case "+" -> calculator.add(num1, num2);
                    case "-" -> calculator.subtract(num1, num2);
                    case "*" -> calculator.multiply(num1, num2);
                    case "/" -> calculator.divide(num1, num2);
                    case "min" -> calculator.min(num1, num2);
                    default -> calculator.max(num1, num2);
                };
            } else if (operation.equals("sqrt")) {
                    System.out.println("Enter a number: ");
                    double num = scanner.nextDouble();
                     result = calculator.sqrt(num);

                } else {
                    System.out.println("Invalid operation");
                    continue;
                }

                System.out.println("Result: " + result);
            }

        scanner.close();
    }
}
