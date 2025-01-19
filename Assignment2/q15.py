side1=float(input("enter side1:"))
side2=float(input("enter side2:"))
side3=float(input("enter side3:"))

if(side1+side2>side3)and (side1+side3>side2)and (side2+side3>side1):
  print("valid triangle")

else:
  print("invalid triangle")  