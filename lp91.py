# Author:Piao Luo
# 函数与过程

def funcTest(x, y):
    return x + y


def proTest():
    print("没有返回值即过程")


def test(x, y):
    print(x, y)


# 不定参数,元组
def test1(*args):
    print(args)


# 默认参数
def test2(x, y=1):
    print(x, ":", y)


# 字典,关键字参数
def test3(**key_value):
    print(key_value)


print(funcTest(1, 2))
proTest()
test(1, 2)  # 与形参位置一一对应
test(y=2, x=1)  # 与形参顺序无关
print(test1(1, 2, 3, 4, 5))
test2(10, 10)
test2(11)
test3(a="aaa", b=2, c=[11, 22, 33])

# lambda匿名函数
res = lambda a, b, c: a + b + c
print(res(1, 2, 3))  # 返回结果为6
