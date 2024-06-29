my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_remove = 'b'

removed_value = my_dict.pop(key_to_remove, None)

if removed_value is not None:
    print(f"Key '{key_to_remove}' removed from dictionary.")
else:
    print(f"Key '{key_to_remove}' not found in dictionary.")

print("Updated dictionary:", my_dict)
