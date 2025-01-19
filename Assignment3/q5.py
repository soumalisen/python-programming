for num in range(1, 501):
    digits = list(map(int, str(num)))
    if sum(d ** 3 for d in digits) == num:
        print(num)
