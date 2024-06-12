def count_characters(string):
    upper_count = 0
    lower_count = 0
    special_count = 0
    numeric_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            numeric_count += 1
        else:
            special_count += 1
    
    print("Cheval will drink 131231 leche!!! oioioi many $$$")
    print(f"Uppercase: {upper_count}")
    print(f"Lowercase: {lower_count}")
    print(f"Numeric: {numeric_count}")
    print(f"Special characters: {special_count}")

count_characters("Cheval will drink 131231 leche!!! oioioi many $$$")
