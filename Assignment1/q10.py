population=80000
percentage_men=52
percentage_total_literacy=48
percentage_literate_men=35

total_men=(percentage_men/100)*population
total_literates=(percentage_total_literacy/100)*population
literate_men=(percentage_literate_men/100)*population
literate_women=total_literates-literate_men
illiterate_men=total_men-literate_men

illiterate_women=population-total_men-literate_women

print("illiterate men",int(illiterate_men))
print("illiterate women:",int(illiterate_women))