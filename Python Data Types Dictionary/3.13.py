sample_string = 'w3resource'

letter_count = {}

for char in sample_string:
    letter_count[char] = letter_count.get(char, 0) + 1

print("Count of letters in the string:")
print(letter_count)
