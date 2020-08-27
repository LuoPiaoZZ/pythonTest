# Author:Piao Luo
# 元组() 列表[]
# count("元素")查询某个元素出现的次数，len(列表或者元组)获取列表或者元组的长度

# 商品列表：元组数组：商品名称 价格
products = [
    ("a", 20),
    ("b", 199),
    ("c", 8)
]
print("商品有：")
# 显示商品的编号、名称、价格
for index, val in enumerate(products):
    print(index, ":", val)

# 用户余额
money = 100
print("用户余额为：", money)

# 购物车：元组数组：商品名称 数量
shop_car = []

while True:
    # 输入添加的商品操作编号
    op_custom = input("请输入添加的商品编号(结算请输入q，退出系统输入其他字符)：")
    if op_custom.isdigit():
        op_custom = int(op_custom)
        if len(products) > op_custom > -1:
            shop_car.append(products[op_custom])
        else:
            print("不存在的商品编号")
    elif op_custom == 'q':
        print("购物车添加商品结束")
        break
    else:
        print("退出系统")
        exit()
print("购物车商品有：")
price = 0
for val in shop_car:
    price += val[1]
    print(val)
print("购物车总价为：", price)
if price < money:
    print("购买成功")
else:
    print("购买失败")
