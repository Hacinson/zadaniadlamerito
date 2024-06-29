def check_integer():
    user_input = input("Input a string: ")
    
    try:
        int_value = int(user_input)

        print("The string is an integer.")
    except ValueError:
        print("The string is not an integer.")

check_integer()
