# Author:Piao Luo
# 编码转换

"""
任何编码转化都会先转成Unicode以后再转化为相应的编码，不同编码之间的中介为Unicode
encode
"""

s = "你好世界"
print(s.encode("gbk"))
print(s.encode("gbk").decode("gbk"))
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8"))
