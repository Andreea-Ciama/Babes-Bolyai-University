from gcdCalculator import *

class GCDApp:
    @staticmethod
    def run():
        while True:
            print("Select a GCD algorithm:")
            print("1. Euclidean Algorithm")
            print("2. Extended Euclidean Algorithm")
            print("3. Binary GCD Algorithm")
            choice = input("Enter the number of the algorithm (1/2/3): ")

            if choice not in ['1', '2', '3']:
                print("Invalid choice. Please enter 1, 2, or 3.")
            else:
                break

        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        calculator = GCDCalculator()

        if choice == '1':
            result = calculator.gcd_euclidean(a, b)
            algorithm = "Euclidean Algorithm"
        elif choice == '2':
            result = calculator.gcd_extended_euclidean(a, b)
            algorithm = "Extended Euclidean Algorithm"
        else:
            result = calculator.arbitrary_size_gcd(a, b)
            algorithm = "Binary GCD Algorithm"

        print(f"GCD of {a} and {b} using {algorithm}: {result}")

if __name__ == "__main__":
    GCDApp.run()