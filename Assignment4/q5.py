def calculate_lcm(a, b):
    lcm = max(a, b)

    while True:
        if lcm % a == 0 and lcm % b == 0:
            break
        lcm += 1

    return lcm
