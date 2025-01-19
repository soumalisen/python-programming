n = int(input("Enter the number of elements: "))
min_num = float('inf')
max_num = float('-inf')

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

range_of_numbers = max_num - min_num
print("Range is:",range_of_numbers)