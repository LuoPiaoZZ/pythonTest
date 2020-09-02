# Author:Piao Luo
"""
装饰器=高阶函数+嵌套函数 本质是函数 为其他函数添加附加功能
原则：不能修改被装饰的函数的源代码、调用方式
"""

import time


# 高阶函数
def log_func(func):
    print("函数开始执行")
    star_time = time.time()
    func  # 带参数就直接写函数名
    time.sleep(2)
    end_time = time.time()
    print("函数执行结束,耗时：", (end_time - star_time))


def log_test(x, y):
    print(x + y)


# 调用高阶函数
log_func(log_test(111, 222))

# 函数当变量
a = log_test
a(12, 21)

# 匿名函数
calu = lambda x, y: x + 3 * y
print(calu(2, 3))


# 嵌套函数
def father_fuc():
    def sub_fuc():
        print("嵌套函数：hello world")

    sub_fuc()


father_fuc()


# 装饰器
def time_log(func):
    def log(*args):
        s = time.time()
        print("开始执行！")
        time.sleep(2)
        func(*args)
        print("结束执行")
        e = time.time()
        print("耗时：", e - s)

    return log  # 带参数就直接写函数名返回即可


@time_log
def my_func1(x, y):
    print("执行ing", x, y)


@time_log
def my_func2(x, y, z):
    print("执行ing", x, y, z)


# 调用方式1
# time_log(my_func(...))
# 调用方式2 语法糖
my_func1(9, 99)
my_func2('a', 'b', 'c')
