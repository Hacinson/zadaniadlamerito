def sum_of_digits(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

s = input("Enter a string: ")
print("Sum of digits in the string:", sum_of_digits(s))
