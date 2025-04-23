def generate_fibonacci(n):
    

    if not isinstance(n, int):
        return "Invalid input. 'n' must be an integer."
    if n < 0:
        return "Invalid input. 'n' must be non-negative."
    if n == 0:
        return []

    fibonacci_series = []
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b  # Efficiently update a and b
    return fibonacci_series


# Get input from the user (with error handling)
while True:
    try:
        num = int(input("Enter a non-negative integer (n): "))
        if num >= 0:
            break  # Exit the loop if input is valid
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

fib_series = generate_fibonacci(num)

if isinstance(fib_series, list):  # Check if it's a list (success)
    print("Fibonacci series:", fib_series)
else:  # It's an error message
    print(fib_series)

