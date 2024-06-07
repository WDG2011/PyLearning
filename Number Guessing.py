# Import random number module
import random

# Generates a random number from 1 to 10
randnum = random.randint(1, 10)
attempts = 0

while attempts < 10:
    guess = int(input("Guess a number from 1 to 10: "))
    attempts += 1  
    
    if guess > randnum:
        print("Too high!")
    elif guess < randnum:
        print("Too small!")
    else:xx
        print("Good job, correct!")
        break  
else:
    print("Sorry, you've reached the maximum number of attempts. The correct number was", randnum)
