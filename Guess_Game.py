# Guessing game
import random
jackpot = random.randint(1, 100)

guess = int(input("Guess Number "))
count = 1
while guess != jackpot:
    if guess < jackpot:
        print("Guess higher num ")
    else:
        print("Guess lower num ")
    guess = int(input("guess number "))
    count += 1
print("Correct Guess")
print("your attempts = ", count)
