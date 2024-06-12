def remove_duplicates(input_string):
    result = ""
    for char in input_string:
        if char not in result:
            result += char
    return result

input_string = "Mississippi"
output_string = remove_duplicates(input_string)
print("Input String:", input_string)
print("Output String:", output_string)
