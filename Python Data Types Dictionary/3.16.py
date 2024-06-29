sample_dict = {
    'first name': 'John',
    'last name': 'Doe',
    'city': 'New York',
    'phone number': '123-456-7890'
}

modified_dict = {key.replace(' ', ''): value for key, value in sample_dict.items()}

print("Dictionary with spaces removed from keys:")
print(modified_dict)
