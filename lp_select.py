# Author:Piao Luo
# 初步筛选端口号过程使用到的程序，需要什么数据想到哪写到哪，缺乏拓展性和普遍性

# 不重复的端口
f134 = open("134.txt", "r", encoding="utf-8")
l134 = []
for index, lineValue in enumerate(f134.readlines()):
    l134.insert(index, lineValue.strip())
print("不重复端口数量：", l134.__len__())
# 未筛选过的端口
f168 = open("168.txt", "r", encoding="utf-8")
l168 = []
for index, lineValue in enumerate(f168.readlines()):
    l168.insert(index, lineValue.strip())
print("总共端口数量：", l168.__len__())

# 初始化重复端口数量均为0
port_count = []
for i in range(l134.__len__()):
    port_count.insert(i, 0)

# 记录重复警告数量
for val in l168:
    for i in range(len(l134)):
        if val == l134[i]:
            port_count[i] += 1

# 打印初步筛选重复警告及端口名称
for index, count in enumerate(port_count):
    if count != 1:
        print(l134[index], ":", count)

# 筛选None
# 获取端口为None的行号
none_num = []
for index, val in enumerate(l168):
    if val == 'None':
        none_num.insert(index, index)
# 设备名称
fnone = open("None.txt", "r", encoding="utf-8")
lnone = []
for index, lineValue in enumerate(fnone.readlines()):
    if index in none_num:
        lnone.insert(index, lineValue.strip())
for val in lnone:
    print(val)
