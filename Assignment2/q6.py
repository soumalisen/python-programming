age1=int(input("enter age of Ram:"))
age2=int(input("enter age of sham:"))
age3=int(input("enter age of ajay:"))

if (age1<age2 and age1<age3):
  print("the youngest is Ram")
elif(age2<age1 and age2<age3):
  print("the youngest is sham")
else:
  print("the youngest is ajay")