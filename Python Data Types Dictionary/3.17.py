my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print("Keys, Values, and Items in the dictionary:")
for key in my_dict:
    value = my_dict[key]
    item = (key, value)
    print(f"Key: {key}, Value: {value}, Item: {item}")
