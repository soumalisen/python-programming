l=float(input("enter the length: "))
b=float(input("enter the breadth: "))
perimeter=2*(l+b)
area=l*b
if area>perimeter:
  print("area of rectangle is greater than perimeter")

elif area<perimeter:
  print("perimeter of rectangle is greater than area")
else:
  print("area and perimeter of rectangle is equal")