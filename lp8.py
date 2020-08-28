# Author:Piao Luo
# 文件操作 读写操作，读取时注意指针位置
# 需要在terminal里面执行，可能pycharm的run没有读取文件权限
import os  # 对文件夹或在文件属性操作的模块

# 网络传输为二进制编码，模式必须要带有b的相关字符串,如 wb+ ab+
file = open("lp8.txt", "a+", encoding="utf-8")  # 文件句柄,读写文件
file.write("\nxxxxxxxxxxxx")
file.flush()
file.write("\n你好世界哈哈哈哈")
file.flush()
# 查找当前指针位置
position = file.tell()
print("指针当前文件位置1 : ", position)
# 把指针再次重新定位到文件开头
position = file.seek(0, 0)
position = file.tell()  # 当前指针位置
print("指针当前文件位置2 : ", position)

# 将默认从当前指针位置开始读取
line = file.readline()  # 行
print("----", line)

for index, lineValue in enumerate(file.readlines()):  # 打印从当前指针开始的数的指定行
    if index == 3:
        print("####", lineValue)
'''
for line in file:  # 此时file已经是迭代器，效率最高，需要行号的话就自己定义一个计数器
    print(line)
'''
file.seek(0, 0)
data = file.read()  # 指针回到起点，打印全文
print("****", data)
# 关闭打开的文件
file.close()

# 对文件夹和文件的操作在os模块中
# 重命名文件
os.rename("lp8.txt", "newlp8.txt")
