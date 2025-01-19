def power(a, b):
    sum = 1
    for i in range (b):
        sum *= a
    return sum
    
print(power(5, 3))