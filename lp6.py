# Author:Piao Luo
# 字典{} key-value 无序，key唯一且不可变（不能为列表）

dict = {
    "a": 1,
    ("c", "b"): 2,
    3: 4,
    "hello": [1, 2],
    "嵌套": {"嵌套+1": [9, 10]}
}
for k in dict:
    print(k, dict[k])
for k, v in dict.items():
    print(k, v)

# 安全获取,无显示为None
print(dict.get("a"))
# 增,修改
dict[0] = 123
print(dict)
dict["嵌套"]["嵌套+1"][0] = 999
print(dict)
# 如果能取到就返回，如果不能就创建一个新的，类似的还有update
dict.setdefault("b", {"A": 1})
print(dict)
# 字典转列表
print(dict.items())
# formkeys 浅拷贝,所有key共享一个value
# 删除
del dict[0]
print(dict)
dict.clear()
print(dict)
del dict
print(dict)
