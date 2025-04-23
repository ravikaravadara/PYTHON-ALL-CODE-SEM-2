#

N = int(input("Enter the value of N: "))

# Printing N natural numbers in reverse
print("The first", N, "natural numbers in reverse order are:")
for i in range(0, -1):
    print(i, end=" ")
print(N)
