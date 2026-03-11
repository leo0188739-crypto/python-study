#双色球是由中国福利彩票发行管理中心发售的乐透型彩票，每注投注号码由6个红色球和1个蓝色球组成。
# 红色球号码从1到33中选择，蓝色球号码从1到16中选择。每注需要选择6个红色球号码和1个蓝色球号码，

red = [i for i in range(1,34)]
blue = [i for i in range(1,17)]
import random
num = int(input('Generate how many numbers:'))
for _ in range(num):
    # 从红色球列表中随机抽出6个红色球（无放回抽样）
    selected_red = random.sample(red, 6)
    selected_red.sort()
    # 输出选中的红色球
    for ball in selected_red:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{random.choice(blue):0>2d}\033[0m')