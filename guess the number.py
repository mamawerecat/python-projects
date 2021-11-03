import random
numbers = range(1, 51)
random_num = random.choice(numbers)
guess = int(input("Guess a number 1-50"))
while guess != random_num:
    if guess > random_num:
        print("Lower")
        guess = int(input("Try again."))
    elif guess < random_num:
        print("Higher")
        guess = int(input("Try again."))
if guess == random_num:
    print("*~*~*~*Winner!!!*~*~*~*")


##By Mamawerecat
