def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Input from user
num = int(input("Enter a natural number: "))
print(f"Factorial of {num} is {factorial(num)}")