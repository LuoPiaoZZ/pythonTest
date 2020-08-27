# Author:Piao Luo
# 变量 多行注释 循环

a = 1
print("1 hello world", a)

'''
我就是个注释
'''

# 默认所有输入都是字符串
name = input("name:")
age = int(input("age:"))
# 多行字符串
info1 = '''
---information---
name:%s
age:%d
''' % (name, age)
print("2.1 ", info1)

info2 = '''
---information---
name:{_name}
age:{_age}
'''.format(_name=name, _age=age)
print("2.2 ", info2)

info3 = '''
---information---
name:{0}
age:{1}
'''.format(name, age)
print("2.3 ", info3)

# 无大括号，需要缩进四行
# if elif else
_n = "lp"
_a = 22
if name == _n and age == _a:
    print("3 successful")
else:
    print("3 error")

if age < 10:
    print("3.1 10")
elif age < 15:
    print("3.1 15")
elif age < 20:
    print("3.1 20")
else:
    print("3.1 ", age)

# while
count = 0
while True:
    count += 1
    print("4 ", count)
    if count == 5:
        break
while count < 10:
    count = count + 1
    print("4 ", count)

# for
for i in range(3):  # 循环3次，0~2，默认步长为1
    print("5.1 ", i)
for i in range(3, 10, 2):  # 3,5,7,9 步长为2
    print("5.2 ", i)
