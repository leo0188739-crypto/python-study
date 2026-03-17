import time


def timer(func):
    """这就是我们的计时装饰器（手机壳）"""

    # wrapper 是一个包装函数，它会把原来的 func 包在里面
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 【加特效：记录开始时间】

        result = func(*args, **kwargs)  # 【核心：真正执行原来的函数】

        end_time = time.time()  # 【加特效：记录结束时间】
        print(f"[{func.__name__}] 运行耗时: {end_time - start_time:.4f} 秒")

        return result  # 把原函数的结果交还出去

    return wrapper  # 把做好的包装函数交出去

@timer
def download_movie():
    print("开始下载电影...")
    time.sleep(2)  # 模拟网络延迟，睡2秒
    print("下载完成！")

# 我们像往常一样调用这个函数，什么都不用改
download_movie()