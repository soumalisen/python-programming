number=int(input("Enter the Five Digits :"))

digit1 = ((number // 10000) + 1) % 10
digit2 = (((number // 1000) % 10) + 1) % 10
digit3 = (((number  // 100) % 10) + 1) % 10
digit4 = (((number // 10) % 10) + 1) % 10
digit5 = ((number % 10) + 1) % 10

new_number = digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5
print("new number is", new_number)