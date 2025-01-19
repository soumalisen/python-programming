positives = negatives = zeros = 0
while True:
    num = input("Enter a number (or 'stop' to end): ")
    if num.lower() == 'stop':
        break
    num = int(num)
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1
    else:
        zeros += 1
print(f"Positives: {positives}, Negatives: {negatives}, Zeros: {zeros}")
