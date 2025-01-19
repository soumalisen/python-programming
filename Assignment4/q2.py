def evenodd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

num=int(input("Enter number to check even odd: "))
print("the number is ",evenodd(num))
