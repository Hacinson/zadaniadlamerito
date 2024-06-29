my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 8}

max_value = max(my_dict.values())
max_key = max(my_dict, key=my_dict.get)

min_value = min(my_dict.values())
min_key = min(my_dict, key=my_dict.get)

print("Maximum value:", max_value)
print("Key with maximum value:", max_key)
print("Minimum value:", min_value)
print("Key with minimum value:", min_key)
