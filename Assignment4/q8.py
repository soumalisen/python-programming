def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def combinatoric(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Input from user
n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(f"C({n}, {r}) = {combinatoric(n, r)}")