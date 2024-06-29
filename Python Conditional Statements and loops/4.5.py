def count_even_odd(numbers):
    count_even = 0
    count_odd = 0
    
    for num in numbers:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    
    # Print the results
    print(f"Number of even numbers: {count_even}")
    print(f"Number of odd numbers: {count_odd}")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

count_even_odd(numbers)
