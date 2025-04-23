def count_alphabets_digits(input_string):
    

    alphabet_count = 0
    digit_count = 0

    for char in input_string:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  
            alphabet_count += 1
        elif '0' <= char <= '9':  
            digit_count += 1

    return alphabet_count, digit_count



input_string = input("Enter a string: ")


alphabets, digits = count_alphabets_digits(input_string)


print("Number of alphabets:", alphabets)
print("Number of digits:", digits)

