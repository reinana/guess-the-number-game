import sys
import random

print("Guess the number from 1 - 10!")
random_number = random.randrange(1, 10, 1)
guess_number = input()
if(guess_number == ''): print("Input your guess number.")
else:
    while(random_number != int(guess_number)) :
        print("Wrong")
        guess_number = input()
        if(guess_number == ''): 
            print("Input your guess number.")
            guess_number = input()
    print("Collect!")