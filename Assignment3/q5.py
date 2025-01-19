# Print all Armstrong numbers between 1 and 500
for num in range(1, 501):
    
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10 
        total += digit ** 3  
        temp //= 10  
    
    
    if total == num:
        print(num)