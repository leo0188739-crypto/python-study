#双色球是由中国福利彩票发行管理中心发售的乐透型彩票，每注投注号码由6个红色球和1个蓝色球组成。
# 红色球号码从1到33中选择，蓝色球号码从1到16中选择。每注需要选择6个红色球号码和1个蓝色球号码，

import random

num = int(input('Generate how many numbers:'))
for _ in range(num):
    select_red = []
    red = list(range(1, 34))
    blue = random.randint(1, 16)
    for _ in range(6):
        index = random.randrange(len(red))
        select_red.append(red.pop(index))
    select_red.sort()
    print(f'\033[031m{select_red}\033[0m;\033[034m[{blue}]')