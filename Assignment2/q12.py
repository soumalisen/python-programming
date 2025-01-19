x=float(input("enter the value of x coordinate of point: "))
y=float(input("enter the value of y coordinate of point: "))

if x==0 and y!=0:
  print("point lies on y axis")

elif y==0 and x!=0:
  print("point lies on x axis")

else:
  print("point does not lies on x,y axis or origin ")    