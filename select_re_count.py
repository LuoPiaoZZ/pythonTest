# Author:Piao Luo
import xlwt
import xlrd


# 将文件内容转化为list
def file_list(file_path):
    file = open(file_path, "r", encoding="utf-8")
    list = []
    for index, lineValue in enumerate(file.readlines()):
        list.insert(index, lineValue.strip())
    # print("存入的数组：", list)
    return list


def file_list1(file_path):
    file = open(file_path, "r", encoding="utf-8")
    list = []
    for index, lineValue in enumerate(file.readlines()):
        list.insert(index, int(lineValue.strip()))
    # print("存入的数组：", list)
    return list


# 比较两个文件内容，得出重复的内容的数量
def diff_count(relist, list):
    # 初始化重复内容的数量为0
    re_count = []
    for i in range(list.__len__()):
        re_count.insert(i, 0)
    # 记录重复数量
    for val in relist:
        for i in range(len(list)):
            if val == list[i]:
                re_count[i] += 1
    print("重复的信息及数量：")
    # 打印筛选重复信息及数量
    # 开始写入
    print("开始写入：")
    res_file = open("users/res.txt", "w", encoding="utf-8")
    res_file.write("用户：出现数量\n")
    for index, count in enumerate(re_count):
        if count != 1:
            res_file.write('''%s:%d''' % (list[index], count))
    res_file.close()
    print("写入结束!")


def diff_count1(relist, list):
    # 初始化重复内容的数量为0
    re_count = []
    for i in range(list.__len__()):
        re_count.insert(i, 0)
    # 记录重复数量
    for val in relist:
        for i in range(len(list)):
            if val == list[i]:
                re_count[i] += 1
    print("重复的信息及数量：")
    # 打印筛选重复信息及数量
    # 开始写入
    print("开始写入：")
    # 创建一个worksheet
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('同名工程')
    line = 0
    for index, count in enumerate(re_count):
        if count != 1:
            worksheet.write(line, 0, list[index])
            worksheet.write(line, 1, count)
            line += 1
    workbook.save("users/同名工程.xlsx")
    print("写入结束!")

    # 创建一个worksheet


# 获取记录行号
def line_num(only_list, all_list):
    res = open("users/同名行号.txt", "w", encoding="utf-8")
    print("开始写入")
    for only in only_list:
        for index, val in enumerate(all_list):
            if only == val:
                res.write('''%d\n''' % index)
    res.close()
    print("结束写入")


# 根据行号写入需要的整条数据
def res_data(line_list, all_list):
    res = open("users/同名数据信息.txt", "w", encoding="utf-8")
    print("开始写入")
    for line in line_list:
        for index, val in enumerate(all_list):
            if int(line) == index:
                res.write('''%s\n''' % val)
    res.close()
    print("结束写入")


def res_excel(old_excel, new_excel, lines):
    print("开始")
    old_sheet = xlrd.open_workbook(old_excel).sheet_by_index(0)
    # 创建一个worksheet
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('同名用户完整信息')
    count = 0
    for line in lines:
        for index in range(old_sheet.nrows):
            if int(line) - 1 == index:
                row = old_sheet.row_values(index)
                for i, content in enumerate(row):
                    worksheet.write(count, i, content)  # 在获得的第一个sheet对象中，第count行，第i列写入content
                count += 1
                break
    workbook.save(new_excel)
    print("结束")


# 测试使用
'''
# 重复的端口名称及数量
relist = file_list("168.txt")  # 未被筛选数据
list = file_list("134.txt")  # 不重复的数据
diff_count(relist, list)

# 重复的设备名称及数量
relist = file_list("relist.txt")  # 未被筛选数据
list = file_list("list.txt")  # 不重复的数据
diff_count(relist, list)
'''

'''
relist = file_list("users/reusers.txt")  # 未被筛选数据
list = file_list("users/users.txt")  # 不重复的数据
diff_count1(relist, list)
'''

'''
relist = file_list("users/reusers.txt")  # 未被筛选数据
list = file_list("users/同名用户.txt")  # 不重复的数据
line_num(list, relist)

relist = file_list("users/all.txt")  # 未被筛选数据
list = file_list("users/同名行号.txt")  # 不重复的数据
res_data(list, relist)
'''
# res_excel("users/2020年7月民资引入分成明细表 (已结算0805) - 副本.xlsx", "users/data.xlsx", file_list("users/同名行号.txt"))
'''
# 获取同名工程数据
relist = file_list("users/项目编号.txt")
list = file_list("users/项目编号不重复.txt")
diff_count1(relist, list)
'''
# 在重名的基础上对同名的工程编号进行比较
'''
思路：将同名数据的excel读取并建立字典，key=用户名,value=重复数量
遍历同名完整信息表，两层循环比较，工程名是否相同，如果相同记录筛选相同的结果
'''


# 将两列数据的excel转化为字典
def dict_excel(excel_path):
    count_dict = {}
    sheet = xlrd.open_workbook(excel_path).sheet_by_index(0)  # 获取excel文件的第一个sheet
    # 遍历读取每一行数据，并存储进字典中
    for row_num in range(sheet.nrows):
        row = sheet.row_values(row_num)
        count_dict[row[0]] = row[1]
    # 返回字典
    return count_dict


# 两层循环比较,得出重复的那些行号
def same_pro(same_name_count_dict, file_name):
    sheet = xlrd.open_workbook(file_name).sheet_by_index(0)  # 获取excel文件的第一个sheet
    # 创建一个worksheet
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('同名同工程名称重复行号')
    count = 0
    for key in same_name_count_dict.keys():
        for row_num in range(sheet.nrows):
            print("行号：", row_num)
            row = sheet.row_values(row_num)
            if key == row[38]:  # 用户名
                index_temp_start = row_num
                index_temp_end_1 = index_temp_start + int(same_name_count_dict[key]) - 1
                for i in range(index_temp_start, index_temp_end_1):
                    for j in range(i + 1, index_temp_end_1 + 1):
                        if j < sheet.nrows and sheet.row_values(i)[3] == sheet.row_values(j)[3]:  # 比较的是工程编号
                            worksheet.write(count, 0, j)
                            count += 1
    workbook.save("users/同名同工程名称重复行号.xlsx")
    print("写入结束！")


'''
test_dict = dict_excel("users/同名信息.xlsx")
same_pro(test_dict, "users/同名完整信息表.xlsx")
'''


def pro_user(lines, old_excel, new_excel):
    old_sheet = xlrd.open_workbook(old_excel).sheet_by_index(0)  # 获取excel文件的第一个sheet
    # 创建一个worksheet
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('同名不同工程名称文件')
    count = 0
    for row_num in range(old_sheet.nrows):
        if row_num not in lines:
            row = old_sheet.row_values(row_num)
            for i, content in enumerate(row):
                worksheet.write(count, i, content)  # 在获得的第一个sheet对象中，第count行，第i列写入content
            count += 1
    workbook.save(new_excel)


def pro_user1(lines, old_excel, new_excel):
    old_sheet = xlrd.open_workbook(old_excel).sheet_by_index(0)  # 获取excel文件的第一个sheet
    # 创建一个worksheet
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('同名不同工程名称文件1')
    count = 0
    for row_num in range(old_sheet.nrows):
        if row_num in lines:
            row = old_sheet.row_values(row_num)
            for i, content in enumerate(row):
                worksheet.write(count, i, content)  # 在获得的第一个sheet对象中，第count行，第i列写入content
            count += 1
    workbook.save(new_excel)


'''
lines = file_list1("users/同名同工程编号的行号.txt")
pro_user1(lines, "users/同名完整信息表.xlsx", "users/同名不同工程最终文件1.xlsx")
'''
