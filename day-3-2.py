#计算机出一个 1 到 100 之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息“大一点”、
# “小一点”或“猜对了”，如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
import random

a = random.randint(1,100)
counter = 0
while True:
    b = int(input('Guess a number between 1 and 100: '))
    counter += 1
    if a < b <= 100:
        print(f'Smaller')
    elif 0 <= b < a:
        print(f'Larger')
    else:
        print(f'Guess correct, total guess : {counter}')
        break

