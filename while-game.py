import sys
import random

print("Guess the number from 1 - 10!")
min_number = int(input("最小値を入力してください \n"))
max_number = int(input("最大値を入力してください \n"))
if min_number >= max_number:
    print("最小値は最大値より小さくしてください")



else:
    guess_number = input("予想値を入力してください \n" )
    random_number = random.randrange(min_number, max_number, 1)
    while(random_number != int(guess_number)) :
        print("Wrong")
        guess_number = input()
        if(guess_number == ''): 
            print("Input your guess number.")
            guess_number = input()
    print("Collect!")
