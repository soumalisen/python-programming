amt = int(input("Enter the Amount to be Withdrawn :"))
hundred = amt//100
amt = amt%100
fifty = amt//50
amt = amt%50
ten = amt//10
print("No of Hundred Notes :",hundred)
print("No of Fifty Notes :",fifty)
print("No of Ten Notes :",ten)
