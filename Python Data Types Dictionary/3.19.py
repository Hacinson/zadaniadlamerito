def check_keys_exist(dictionary, keys):
    for key in keys:
        if key not in dictionary:
            return False
    return True

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

keys_to_check = ['a', 'b', 'e']

keys_exist = check_keys_exist(my_dict, keys_to_check)

print(f"Keys {keys_to_check} exist in the dictionary: {keys_exist}")
