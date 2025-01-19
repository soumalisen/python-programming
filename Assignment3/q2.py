n = int(input("Enter a number to find its factorial: "))
result = 1
for i in range(1, n + 1):
    result *= i
print(f"Factorial of {n} is {result}")