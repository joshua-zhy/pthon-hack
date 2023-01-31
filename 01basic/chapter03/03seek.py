# 12.5 文件的定位读写（tell函数、seek函数）
 
# tell()：返回文件指针的当前位置

# 直接上栗子，一看就懂：

# dong.txt文件中的内容是：hello,world

file = open("dong.txt", "r")
words = file.read(4)
print(f'读取的数据是：{words}')  # hell
# 查找当前位置
position = file.tell()
print(f'当前位置是：{position}')  # 4


words = file.read(5)
print(f'读取的数据是：{words}')   # o,wor
position = file.tell()
print(f'当前位置是：{position}')  # 9
 
# seek()：从指定位置开始读取或者写入文件的数据

'''
语法：文件对象.seek（偏移量，起始位置）
起始位置：0 文件开头  1 当前位置  2 文件结尾
作用：用来移动文件指针

目标：
    1. r模式 ：改变文件指针位置，改变读取数据开始位置或把文件指针放结尾（无法读取数据）
    2. o模式 ： 改变文件指针位置，做到可以读取出来数据
'''

# test.txt文件的内容是：aaaaa

f = open('test.txt', 'r+')

# 1. 改变读取数据开始位置
# f.seek(2,0)   # 从第三个a开始读取
f.seek(0,2)   # 指针到了文件结尾，读取不出来数据
con = f.read()
print(con)

# 把文件指针放结尾（无法读取数据）
# f.seek(0, 2)

# 2. a 改变文件指针位置，做到可以读取出来数据
f.seek(0,0)  # 这时指针跑到了开头，这时可以读出数据
# f.seek(0)   # 如果是两个0，可以省略写一个0
con = f.read()
print(con)
f.close()

