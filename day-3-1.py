#输入两个正整数求它们的最大公约数
a = int(input('a = '))
b = int(input('b = '))
for i in range(a,0,-1):
    if a % i == 0 and b % i == 0:
        print(f"最大公约数: {i}")
        break

