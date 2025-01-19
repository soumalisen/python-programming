num=int(input("enter a five digit number: "))
a=num
sum=0
while(num>0):
  rem=num%10
  sum=(sum*10)+rem
  num=num//10

if(a==sum):
  print("equal")

else:
  print("not equal")  