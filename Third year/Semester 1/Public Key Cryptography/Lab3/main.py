import math

# Function to calculate the integer square root of a number
def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

# Function implementing Generalized Fermat's Factorization Algorithm
def generalized_fermat(n):
    k = 1
    while True:
        # Find the ceiling of the square root of (k * n)
        t0 = math.ceil(isqrt(k * n))
        counter = 0
        t = t0 + counter
        # Calculate the square root of (t^2 - k * n)
        temp = isqrt((t * t) - (k * n))
        # Iterate until a solution is found or a counter limit is reached
        while temp * temp != (t * t) - (k * n) and counter < 1000:
            counter += 1
            t = t0 + counter
            temp = isqrt((t * t) - (k * n))
        # If a solution is found, calculate the factors p and q
        if temp * temp == (t * t) - (k * n):
            s = temp
            p = t + s
            q = t - s
            return p, q
        k += 1

# Main program
print("Enter the number to factor of the form (p*q): ")
n = int(input())
# Check for invalid input (even number or perfect square)
if n % 2 == 0 or math.isqrt(n)**2 == n:
    print("Invalid input. Please enter an odd number that is not a perfect square.")
else:
    # Call the factorization function
    p, q = generalized_fermat(n)
    # Display the factors
    print("Your first number   : ", int(p))
    print("Your Second number  : ", int(q))
