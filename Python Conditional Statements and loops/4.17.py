def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_next_day():
    year = int(input("Input a year: "))
    month = int(input("Input a month [1-12]: "))
    day = int(input("Input a day [1-31]: "))

    if month < 1 or month > 12 or day < 1 or day > 31:
        print("Invalid input. Please enter valid year, month, and day.")
        return

    leap_year = is_leap_year(year)

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    elif month == 2:
        max_days = 29 if leap_year else 28

    if day > max_days:
        print(f"Invalid input. There are {max_days} days in month {month}.")
        return

    if day < max_days:
        next_day = day + 1
        next_month = month
    else:
        next_day = 1
        if month < 12:
            next_month = month + 1
        else:
            next_month = 1
            year += 1

    next_date = f"{year}-{next_month}-{next_day}"
    print(f"The next date is [yyyy-mm-dd] {next_date}")

get_next_day()
