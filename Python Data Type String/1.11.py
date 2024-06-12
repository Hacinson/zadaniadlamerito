def max_characters(s):
    max_char = ""
    max_count = 0
    
    for char in set(s):
        count = s.count(char)
        if count > max_count:
            max_count = count
            max_char = char
    
    return max_count


string = "cheval drinks la leche"
print(max_characters(string))
