# 12.6 文件备份
# 1. 用户输入目标文件
old_name = input('请输入您要备份的文件名：')
print(old_name)

# 2. 规划备份文件的名字
# 2.1 提取后缀 -- 找到名字中的点 -- 名字和后缀分离 -- 最右侧的点才是后缀的点 -- 字符串查找某个字串rfind
index = old_name.find('.')


# 4. 进行优化：有效文件才备份  .txt这个文件名就不是有效的
if index > 0:
    # 提取后缀
    postfix = old_name[index:]

# 2.2 组织新名字 = 原名字 + [备份] + 后缀
# 原名字就是字符串的一部分字串 -- 切片[开始：结束：步长]
print(old_name[:index])    # 开始从0开始，可以省略不用写
print(old_name[index:])    # 因为提取到最后，所以后面可以省略
# new_name = old_name[:index] + '[备份]' + old_name[index:]
new_name = old_name[:index] + '[备份]' + postfix   # 如果用户输入的文件名不符合，则会报错
print(new_name)


# 3. 备份文件导入数据（数据和源文件一样）
# 对于计算机来讲，我们存储什么，对于底层，他都是以二进制形式做的存储以及操作，用二进制打开没有问题的。
# 3.1 打开原文件和备份原文件
old_f = open(old_name, 'rb')
new_f = open(new_name,'wb')

# 3.2 原文件读取，备份文件写入
# 如果不确定目标文件大小，循环读取写入，当读取出来的数据没有了，终止循环
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        # 表示读取完成了
        break
    new_f.write(con)
    
# 3.3 关闭文件
old_f.close()
new_f.close()

