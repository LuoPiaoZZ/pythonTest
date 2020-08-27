# Author:Piao Luo
# 字符串

name = "lplplplp"
# 首字母大写
print(name.capitalize())
# 计算字符串某段（左闭右开）某个字母出现次数
print(name.count("p", 0, 6))
# 是否以什么结尾
print(name.endswith("lp"))
# 返回查找的元素的索引
print(name.find("l"))
# 是否是数字
print(name.isdigit())
# 字符串列表变成字符串
print(''.join(["11", "2", "3"]))  # 1123
print(','.join(["1", "2", "3"]))  # 1,2,3
# 头部，尾部填充,使总长为50
print(name.center(50, "-"))
print(name.ljust(50, "#"))
print(name.rjust(50, "*"))
# 大小写
print(name.upper(), ":", name.lower())
# 去除空格
print("  你好  ", "###")
print("  你好  ".strip(), "###")
# 字符串转字节，默认utf-8
print(name.encode())
# 对应字符翻译
trans=str.maketrans("abcdefg", "1234567")
print("gabcdee", "gabcdee".translate(trans))  # gabcdee 7123455
# 替换
print(name.replace("p", "PP", 1))
# 交换大小写
print(name.swapcase())

