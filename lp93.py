# Author:Piao Luo
# 生成器 由于内存有限，对一些有规律的列表，进行一边循环一边计算，只有在调用的时候才会生成，且只记录当前位置，节约内存
# 列表生成式
list = [i * 2 for i in range(10)]
print(list)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# 斐波那契
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1


fib(5)


# 生成器
def fib1(max1):
    n, a, b = 0, 0, 1
    while n < max1:
        yield b
        a, b = b, a + b
        n += 1


f = fib1(100) # 生成器
print(f.__next__())
print(f.__next__())
print(f.__next__())
