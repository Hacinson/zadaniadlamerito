my_dict = {
    'group1': ['apple', 'banana', 'orange'],
    'group2': ['pear', 'grape', 'kiwi'],
    'group3': ['cherry', 'plum', 'mango']
}

sorted_dict = {key: sorted(value) for key, value in my_dict.items()}

print("Sorted dictionary:")
for key, value in sorted_dict.items():
    print(f"{key}: {value}")
