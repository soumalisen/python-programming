for i in range(1, 11):
    hours = float(input(f"Enter hours worked above 40 for employee {i}: "))
    overtime_pay = hours * 12.0
    print(f"Employee {i} overtime pay: Rs. {overtime_pay}")
