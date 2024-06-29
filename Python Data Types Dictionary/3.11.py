my_dict = {'a': 100, 'b': 200, 'c': 50, 'd': 300, 'e': 150}

sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

highest_values = sorted_dict[:3]

print("Highest 3 values of corresponding keys:")
for key, value in highest_values:
    print(f"{key}: {value}")
 
