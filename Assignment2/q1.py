cp=float(input("enter cp: "))
sp=float(input("enter sp:"))
if sp>cp:
  profit=sp-cp
  print("profit is:",profit)

elif sp<cp:
  loss=cp-sp
  print("loss is:",loss)

else:
  print("no profit,no loss")   