number=int(input("Enter a five digit number: "))
digit1=number%10
digit2=(number//10)%10
digit3=(number//100)%10
digit4=(number//1000)%10
digit5=(number//10000)%10

sum_of_digits=digit1+digit2+digit3+digit4+digit5
print("sum of the digits=",sum_of_digits)