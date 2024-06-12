def count_repeated_chars(string):
    char_count = {}
    repeated_chars = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for key, value in char_count.items():
        if value > 1:
            repeated_chars[key] = value

    return repeated_chars

string = "cheval drinks la leche"
result = count_repeated_chars(string)
print(result)
