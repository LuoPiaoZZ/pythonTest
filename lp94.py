# Author:Piao Luo
# json 序列化与反序列化
import json

info = {
    'name': 'lp',
    'age': 22
}
f = open('lp94.text', "w+", encoding='utf-8')  # 涉及文件操作不要使用IDE自带的运行，权限不够，需要在terminal里面用命令行运行
# f.write(info.__str__())
# f.seek(0, 0)
# data = eval(f.read())
# print(data, data['age'])
f.write(json.dumps(info))  # 1
f.seek(0, 0)
data = json.loads(f.read())  # 2
print(data, data['age'])
f.close()
