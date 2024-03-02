# Import required modules
import timeit
import random
from gcdCalculator import GCDCalculator  # Import the GCDCalculator class from gcdCalculator module

class GCDPerformanceAnalyzer:
    def __init__(self, algorithms, input_size=10):
        # Constructor to initialize the GCDPerformanceAnalyzer object
        self.algorithms = algorithms  # List of GCD algorithms to analyze
        self.input_size = input_size  # Number of input pairs to generate for analysis
        # Generate random input pairs and store them in a list
        self.input_pairs = [(random.randint(1, 1000), random.randint(1, 1000)) for _ in range(input_size)]

    def measure_time(self, algorithm, a, b):
        # Measure the running time of a specific GCD algorithm for a given input pair
        calculator = GCDCalculator()  # Create an instance of the GCDCalculator class

        if algorithm == '1':
            # For Euclidean Algorithm
            func = lambda: calculator.gcd_euclidean(a, b)
            algorithm_name = "Euclidean Algorithm"
            gcde=calculator.gcd_euclidean(a, b)
            # Measure the execution time of the specified algorithm for 10,000 iterations
            time_taken = timeit.timeit(func, number=10000)
            print(f"Time taken for {algorithm_name}: {time_taken:.6f} seconds and the gcd is  {gcde}")
        elif algorithm == '2':
            # For Extended Euclidean Algorithm
            func = lambda: calculator.gcd_extended_euclidean(a, b)
            algorithm_name = "Extended Euclidean Algorithm"
            gcdee =calculator.gcd_extended_euclidean(a, b)
            # Measure the execution time of the specified algorithm for 10,000 iterations
            time_taken = timeit.timeit(func, number=10000)
            print(f"Time taken for {algorithm_name}: {time_taken:.6f} seconds and the gcd is  {gcdee}")

        else:
            # For Binary GCD Algorithm
            func = lambda: calculator.arbitrary_size_gcd(a, b)
            algorithm_name = "Binary GCD Algorithm"
            gcdb = calculator.arbitrary_size_gcd(a, b)
            # Measure the execution time of the specified algorithm for 10,000 iterations
            time_taken = timeit.timeit(func, number=10000)
            print(f"Time taken for {algorithm_name}: {time_taken:.6f} seconds and the gcd is  {gcdb}")


    def analyze(self):
        # Perform comparative running-time analysis for multiple input pairs and algorithms
        for i, (a, b) in enumerate(self.input_pairs, 1):
            print(f"Analysis for Input {i}: ({a}, {b})")
            for algorithm in self.algorithms:
                self.measure_time(algorithm, a, b)  # Measure time for each algorithm and input pair
                print()

# Example usage of the GCDPerformanceAnalyzer class
algorithms = ['1', '2', '3']  # Algorithm choices: '1' for Euclidean, '2' for Extended Euclidean, '3' for Binary GCD
analyzer = GCDPerformanceAnalyzer(algorithms, input_size=10)  # Create an instance of the GCDPerformanceAnalyzer class
analyzer.analyze()  # Perform the analysis
