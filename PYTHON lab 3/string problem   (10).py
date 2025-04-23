def factorial(n):
    
    if n < 0:
        return "Factorial is not defined for negative numbers."  # Handle negative input
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


# Get input from the user
try:  # Use a try-except block to handle potential ValueError
    num = int(input("Enter a non-negative integer: "))
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")


