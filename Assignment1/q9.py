number = int(input("Enter a four-digit number: "))

last_digit=number%10
first_digit=number//1000
sum_of_digits=first_digit+last_digit
print("sum of the first and last digit is:",sum_of_digits)
