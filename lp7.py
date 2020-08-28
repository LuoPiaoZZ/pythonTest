# Author:Piao Luo
# 集合set 无序 交并差

list1 = [1, 2, 3, 4, 5]
set1 = set(list1)

list2 = [2, 3, 4, 6, 7]
set2 = set(list2)

# 交集 a&b
set_inter = set1.intersection(set2)
print(set_inter)  # 2,3,4

# 并集 a|b
set_union = set1.union(set2)  # set_union = set1.union(set2)
print(set_union)

# 差集 a-b
set_dif1 = set1.difference(set2)  # 1,5
set_dif2 = set2.difference(set1)  # 6,7
print(set_dif1, set_dif2)

# 对称差集 a^b
set_sym_dif = set1.symmetric_difference(set2)  # 1,5,6,7
print(set_sym_dif)

# 子集
set_sub = set1.issubset(set2)  # False
print(set_sub)

# 添加
set1.add(12)  # 单项
set1.update([1, 7, 9])  # 多项 重复则不添加
print(set1)

# 删除
set1.remove(12)  # 移除一项,不存在会报错
set1.discard(9)  # 移除一项,不存在不会报错
print(set1)
# 随即删除
set1.pop()
print(set1)

# 存在
print(12 in set1)
