my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 4, 'd': 5, 'b': 6}

unique_dict = {key: value for key, value in reversed(my_dict.items())}

print("Dictionary with duplicates removed:", unique_dict)
