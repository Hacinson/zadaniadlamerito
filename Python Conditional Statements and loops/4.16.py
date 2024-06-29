def find_median():
    num1 = float(input("Input first number: "))
    num2 = float(input("Input second number: "))
    num3 = float(input("Input third number: "))

    if num1 >= num2 >= num3 or num3 >= num2 >= num1:
        median = num2
    elif num2 >= num1 >= num3 or num3 >= num1 >= num2:
        median = num1
    else:
        median = num3

    print(f"The median is {median}")

find_median()
