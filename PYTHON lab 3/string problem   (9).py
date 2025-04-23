import math

def nCr(n, r):
    """Calculates nCr (combinations)."""
    if r < 0 or r > n:
        return 0  # Handle invalid input
    if r == 0 or r == n:
        return 1
    if r > n // 2:  # Optimization: nCr(n, r) = nCr(n, n-r)
        r = n - r
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)  # Integer division for efficiency
    return result


def nPr(n, r):
    """Calculates nPr (permutations)."""
    if r < 0 or r > n:
        return 0  # Handle invalid input
    result = 1
    for i in range(r):
        result *= (n - i)
    return result


# Get input from the user
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

# Calculate and print nCr and nPr
combinations = nCr(n, r)
permutations = nPr(n, r)

print(f"{n}C{r} = {combinations}")
print(f"{n}P{r} = {permutations}")

