# Author:Piao Luo

import copy

name0 = [1, 2]
name1 = ["a", "b", "c", ["aa", "bb"]]

# 增
name0.insert(0, "3")
name0.insert(0, 3)
print("1", name0)

# 删
del name0[0]
print("2", name0)

# 改
name0[0] = "update"
print("3", name0)

# 查
print("4", name0[0], ": ")
for val in name0:
    print(val)

# 切片:浅拷贝
print("5", name1[:2])

# 拼接
name0.extend(name1)
print("6", name0)

# 反转
name0.reverse()
print("7", name0)

# 浅拷贝 只是引用,简单的使用原来元素的地址
name2 = name0.copy()
name0[0][0] = "copy"
print(name0, "--", name2)

# 深拷贝
name3 = copy.deepcopy(name0)
name0[0][0] = "deepcopy"
print(name0, "--", name3)
