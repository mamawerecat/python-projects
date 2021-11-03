import random
numbers = range(1, 21)
random_num = random.choice(numbers)
guess = int(input("Guess a number 1-20"))
while guess != random_num:
    if guess > random_num:
        print("Lower")
        guess = int(input("Try again. Guess a lower number 1-20"))
    elif guess < random_num:
        print("Higher")
        guess = int(input("Try again. Guess a higher number 1-20"))
if guess == random_num:
    print("Winner!!!")


##By Mamawerecat
