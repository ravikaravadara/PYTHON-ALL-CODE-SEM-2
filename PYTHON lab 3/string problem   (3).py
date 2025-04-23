# Method 1: Using a loop and ASCII values

print("Uppercase Alphabets:")
for char_code in range(ord('A'), ord('Z') + 1):  # ASCII values for A-Z
    print(chr(char_code), end=" ")  # Convert ASCII to character and print
print()  # Newline

print("\nLowercase Alphabets:")
for char_code in range(ord('a'), ord('z') + 1):  # ASCII values for a-z
    print(chr(char_code), end=" ")
print()


# Method 2: Using string constants

import string

print("\nUppercase Alphabets (using string.ascii_uppercase):")
print(string.ascii_uppercase)

print("\nLowercase Alphabets (using string.ascii_lowercase):")
print(string.ascii_lowercase)


# Method 3: List comprehension (more concise)

print("\nUppercase Alphabets (list comprehension):")
print(" ".join([chr(i) for i in range(ord('A'), ord('Z') + 1)]))  # Join for space separation

print("\nLowercase Alphabets (list comprehension):")
print(" ".join([chr(i) for i in range(ord('a'), ord('z') + 1)]))


# Method 4:  Using map and chr (functional approach)

print("\nUppercase Alphabets (map and chr):")
print(" ".join(map(chr, range(ord('A'), ord('Z') + 1))))

print("\nLowercase Alphabets (map and chr):")
print(" ".join(map(chr, range(ord('a'), ord('z') + 1))))
