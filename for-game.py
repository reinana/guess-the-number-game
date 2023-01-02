import sys
import random

print("Guess the number!")
try:
    n = int(input("最小値を入力してください \n"))
    m = int(input("最大値を入力してください \n"))
except ValueError:
    print("数字を入力してください")
    sys.exit()


if n >= m:
    print("最小値は最大値より小さくしてください")
else:
    random_number = random.randrange(n, m, 1)
    for i in range(5):

        try:
            guess_number = int(input("予想値を入力してください\n"))
        except ValueError:
            print("数字を入力してください")
            sys.exit()
        if random_number != guess_number :
            print("Wrong")
        else:
            print("Collect!")
            break
