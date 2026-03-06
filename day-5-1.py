#CRAPS赌博游戏
#说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，
#玩家通过摇两粒骰子获得点数进行游戏。简化后的规则是：玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
#玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
#玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；
#如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。
#为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，每局游戏开始之前，玩家先下注，
#如果玩家获胜就可以获得对应下注金额的奖励，如果庄家获胜，玩家就会输掉自己下注的金额。
#游戏结束的条件是玩家破产（输光所有的赌注）。
import random

balance = 1000
while balance > 0:
    print(f'Your balance : {balance}$')
    while True:
        bet = int(input('bet amount: '))
        if 0 < bet <= balance:
            break
        if bet > balance:
            print(f'You cannot bet exceeds balance : {balance}')
        if bet <= 0:
            print(f'bet amount must be greater than 0')
    print(f'Player bet amount : {bet}$')
    first = random.randint(1,6) + random.randint(1,6)
    print(f'Player get: {first}')
    if first == 7 or first == 11:
        balance += bet
        print(f'Player win, your balance : {balance}$')
    elif first == 2 or first == 3 or first == 12:
        balance -= bet
        print(f'Player lose, your balance : {balance}$')
    else:
        while True:
            second = random.randint(1,6) + random.randint(1,6)
            print(f'Player get: {second}')
            if second == 7:
                balance -= bet
                print(f'Player lose, your balance : {balance}$')
                break
            elif second == first:
                balance += bet
                print(f'Player win, your balance : {balance}$')
                break
            else:
                continue
print(f'Game over, your balance : {balance}$')


