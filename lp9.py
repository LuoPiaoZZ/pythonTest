# Author:Piao Luo
# 文件修改并另存

file1 = open("lp8.txt", "r", encoding="utf-8")
file2 = open("lp9.txt", "w", encoding="utf-8")
for line in file1:
    if "一切，都在意料之中" in line:
        line = line.replace("一切", "ABC")
    file2.write(line)
file1.close()
file2.close()

# with可以自动关闭文件
with open("lp9.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)
