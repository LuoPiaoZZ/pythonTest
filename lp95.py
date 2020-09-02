# Author:Piao Luo
# 二进制形式的序列化和反序列化
import pickle


def func1():
    print("你好，世界")


info = {
    "name": "lp",
    "age": 22,
    "func": func1
}

f = open("lp95.text", "wb+")
f.write(pickle.dumps(info))
f.seek(0, 0)
data = pickle.loads(f.read())
# 打印反序列化数据
print(data)
# 执行反序列化数据里面的函数
data["func"]()
f.close()
