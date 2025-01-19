days_late=int(input("enter the number of days late: "))

if days_late<=5:
  fine=days_late*0.5
  print("fine:",fine,"rupees")

elif days_late<=10:
  fine=(5*0.5)+(days_late-5)*1
  print("fine:",fine,"rupees")



elif days_late<=30:
  fine=(5*0.5)+(5*1)+(days_late-10)*5
  print("fine:",fine,"rupees")

else:
  print("membership cancelled")      