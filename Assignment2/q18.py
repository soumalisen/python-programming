age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").lower()
city = input("Belong to city (Y/N): ").lower()
health = input("Enter health condition Excellent(E) or Poor(P): ").lower()

if health == "e" and 25 <= age <= 35 and city == "y":
    if gender == "m":
        print("Premium is Rs. 4 per thousand; Maximum policy amount is Rs. 2 lakhs")
    elif gender == "f":
        print("Premium is Rs. 3 per thousand; Maximum policy amount is Rs. 1 lakh")
    else:
        print("Not insured")
elif health == "p" and 25 <= age <= 35 and city == "n" and gender == "m":
    print("Premium is Rs. 6 per thousand; Maximum policy amount is Rs. 10,000")
else:
    print(" person Not insured")