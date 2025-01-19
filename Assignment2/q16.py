side1=float(input("enter side1: "))
side2=float(input("enter side2: "))
side3=float(input("enter side3:"))

if side1==side2==side3:
  print("equilateral triangle")

elif side1==side2 or side2==side3 or side1==side3:
  print("Isosceles triangle")

elif(side1**2==side2**2+side3**2 or side2**2==side1**2+side3**2 or side3**2==side1**2+side2**2):
  print("right angle triangle")
else:
  print("scalene triangle")