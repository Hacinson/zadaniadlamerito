def print_lower_lines():
    lines = []
    
    while True:
        line = input("Enter a line (blank line to terminate): ")

        if line == "":
            break

        lines.append(line.lower())

    print("\nLines in lowercase:")
    for line in lines:
        print(line)

print_lower_lines()
