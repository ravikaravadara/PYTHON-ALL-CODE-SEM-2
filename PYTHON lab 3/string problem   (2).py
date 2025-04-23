import math

def sin_approximation(x, terms=10):
    

    result = 0
    for n in range(terms):
        term = (-1)**n * x**(2*n + 1) / math.factorial(2*n + 1)
        result += term
    return result



try:
    x = float(input("Enter the angle in radians: "))
    num_terms = int(input("Enter the number of terms to use (optional, default=10): ") or 10) 
    approx_sin = sin_approximation(x, num_terms)
    actual_sin = math.sin(x)

    print(f"Approximated sin({x}) (using {num_terms} terms): {approx_sin}")
    print(f"Actual sin({x}): {actual_sin}")
    print(f"Difference: {abs(approx_sin - actual_sin)}")

except ValueError:
    print("Invalid input. Please enter a valid number for the angle and an integer for the number of terms.")


