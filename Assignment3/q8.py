num = int(input("Enter a number: "))
result = ""
while num > 0:
    result = str(num % 8) + result
    num //= 8
print(f"Octal equivalent is {result}")
