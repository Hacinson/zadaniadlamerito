my_dict = {'b': 3, 'a': 1, 'c': 2}

sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}

print("Sorted dictionary by key:", sorted_dict)
