import operator
import functools

def calc(init_value, op_func, *args, **kwargs):
    """一个超级万能的流水线计算器"""
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result
# 告诉偏函数：拿 calc 做底模，把它的第 1 个参数锁死为 0，第 2 个参数锁死为加法
sum_all = functools.partial(calc, 0, operator.add)
# 告诉偏函数：拿 calc 做底模，把它的第 1 个参数锁死为 1，第 2 个参数锁死为乘法
mul_all = functools.partial(calc, 1, operator.mul)
# 现在求和只需这样写：
print(sum_all(1, 2, 3))        # 瞬间输出 6
print(sum_all(10, 20, 30))     # 瞬间输出 60

# 现在连乘只需这样写：
print(mul_all(2, 3, 4))        # 瞬间输出 24