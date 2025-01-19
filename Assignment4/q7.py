def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

# Input from user
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")