class GCDCalculator:
    @staticmethod
    def gcd_euclidean(a, b):
        # Use the Euclidean Algorithm to find the GCD of two numbers.
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def extended_gcd(a, b):
        # Use the Extended Euclidean Algorithm to find the GCD of two numbers.
        if a == 0:
            # If a is 0, the GCD is b, and we return it along with coefficients 0 and 1.
            return (b, 0, 1)
        else:
            # Recursive call to find GCD, along with coefficients x and y.
            gcd, x, y = GCDCalculator.extended_gcd(b % a, a)
            return (gcd, y - (b // a) * x, x)

    @staticmethod
    def gcd_extended_euclidean(a, b):
        # Calculate GCD using Extended Euclidean Algorithm, returning only the GCD.
        gcd, x, y = GCDCalculator.extended_gcd(a, b)
        return gcd

    @staticmethod
    def gcd_binary(a, b):
        # Use the Binary GCD Algorithm to efficiently compute the GCD of two numbers.
        if a == b:
            # If both numbers are the same, the GCD is that number.
            return a
        if a == 0:
            # If one of the numbers is 0, the GCD is the other number.
            return b
        if b == 0:
            return a
        if not a & 1:  # If a is even
            if b & 1:  # If b is odd
                # Recursively divide a by 2, leaving b unchanged.
                return GCDCalculator.gcd_binary(a >> 1, b)
            else:  # If both a and b are even
                # Recursively divide both a and b by 2 and multiply the result by 2.
                return GCDCalculator.gcd_binary(a >> 1, b >> 1) << 1
        if not b & 1:  # If a is odd, and b is even
            # Recursively divide b by 2, leaving a unchanged.
            return GCDCalculator.gcd_binary(a, b >> 1)
        if a > b:
            # If both a and b are odd and a > b, subtract b from a and divide the result by 2.
            return GCDCalculator.gcd_binary((a - b) >> 1, b)
        # If both a and b are odd and a <= b, subtract a from b and divide the result by 2.
        return GCDCalculator.gcd_binary(a, (b - a) >> 1)

    @staticmethod
    def arbitrary_size_gcd(a, b):
        # Ensure that a is greater than or equal to b when calling gcd_binary.
        if a < b:
            a, b = b, a
        return GCDCalculator.gcd_binary(a, b)

