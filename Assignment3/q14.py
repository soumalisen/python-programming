machine_cost = 6000
salvage_value = 2000
annual_earning = 1000
alternate_rate = 0.12
years = 0
while True:
    total_earning = annual_earning * years + salvage_value
    alternate_earning = machine_cost * (1 + alternate_rate) ** years
    if total_earning >= alternate_earning:
        break
    years += 1
print(f"Minimum life of the machine: {years} years")
