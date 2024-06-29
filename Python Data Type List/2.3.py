numbers = [1, 2, 3, 4, 5]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print("Largest number in the list:", largest_number)
