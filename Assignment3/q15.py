for i in range(1, 11):
    p = float(input("Enter principal amount: "))
    q = int(input("Enter number of times interest is compounded per year: "))
    r = float(input("Enter rate of interest (in %): "))
    n = int(input("Enter number of years: "))
  
    a = p * (1 + r / (100 * q)) ** (q * n)
    
    
    compound_interest = round(a - p, 2)
    
    print(f"Compound Interest is: {compound_interest}")
    print(f"Final Amount is: {round(a, 2)}")