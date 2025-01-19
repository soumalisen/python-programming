total_sticks = 21
while total_sticks > 1:
    user_pick = int(input("Pick 1, 2, 3, or 4 matchsticks: "))
    if user_pick not in [1, 2, 3, 4]:
        print("Invalid choice. Choose between 1 and 4.")
        continue
    total_sticks -= user_pick
    computer_pick = 5 - user_pick
    print(f"Computer picked {computer_pick} matchsticks.")
    total_sticks -= computer_pick
    print(f"Matchsticks left: {total_sticks}")
print("You are forced to pick the last matchstick. You lose!")
