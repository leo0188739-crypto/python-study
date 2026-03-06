#将一颗色子掷6000次，统计每种点数出现的次数
import random
list = [0]*6
for _ in range(6000):
    a = random.randint(1, 6)
    list[a - 1] += 1
for a in range(1,7):
    print(f'{a} appears {list[a - 1]} times')