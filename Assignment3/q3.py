base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
for _ in range(exp):
    result *= base
print(f"{base} raised to the power of {exp} is {result}")
