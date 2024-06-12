def check_alphabet(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False
    return True

string = input("Enter a string: ")
if check_alphabet(string):
    print("The string contains all the letters of the alphabet.")
else:
    print("The string does not contain all the letters of the alphabet.")
