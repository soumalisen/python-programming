
year = int(input("Enter the year: "))

years_since_1900 = year - 1900


if year < 1900:
    print("Please enter a year greater than or equal to 1900.")
else:
    leap_years = (years_since_1900 // 4) - (years_since_1900 // 100) + (years_since_1900 // 400)

    
    total_days = years_since_1900 * 365 + leap_years

    
    day_of_week = total_days % 7

    
    if day_of_week == 0:
        print("1st January", year, "is a Monday.")
    elif day_of_week == 1:
        print("1st January", year, "is a Tuesday.")
    elif day_of_week == 2:
        print("1st January", year, "is a Wednesday.")
    elif day_of_week == 3:
        print("1st January", year, "is a Thursday.")
    elif day_of_week == 4:
        print("1st January", year, "is a Friday.")
    elif day_of_week == 5:
        print("1st January", year, "is a Saturday.")
    elif day_of_week == 6:
        print("1st January", year, "is a Sunday.")