numbers = [1, 2, 3, 4, 5]

smallest_number = numbers[0]

for number in numbers:
    if number < smallest_number:
        smallest_number = number

print("Smallest number in the list:", smallest_number)
