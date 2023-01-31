'''
在python中要操作文件和文件夹的话，要借助模块，要借助os模块。
1. 导入模块os
2. 使用模块内功能
'''
import os   # 导入模块，借助os模块里面的相关功能。使用os模块相关功能：os.函数名()

# 1. rename(目标文件，新文件名): 重命名
# rename的第一个参数其实是路径，因为这里直接在当前目录下，所以直接写的文件名
# os.rename('1.txt','1000.txt')   # 此时文件已经改名



# 2. remove(目标文件名)
# os.remove('1000.txt')   # 此时1000.txt文件已经删除，如果要删除的文件不存在则会报错



# 3. mkdir(文件夹名字):创建文件夹    也可以带路径的文件夹名字
# os.mkdir('aa')  # 创建文件夹成功


# 4.rmdir(文件夹名字): 删除文件夹
# os.rmdir('aa')  # 删除成功



# 5. getcwd()：返回当前文件所在目录路径
print(os.getcwd())  # 输出 D:\PycharmProjects\pythonProject11



# 6. chdir(目录)改变目录路径
# os.mkdir('aa')  # 创建aa文件夹
# 需求：在aa里面创建bb文件夹：1. 切换目录到aa  2.在aa文件夹中创建bb
# os.chdir('aa')  # 切换到aa文件夹
# os.mkdir('bb')  # 在文件夹中创建bb



# 7. listdir(目录): 获取某个文件夹下所有文件，返回一个列表
# print(os.listdir())  # 如果没有填写目录，那么显示当前文件所在的文件夹下所有文件
# print(os.listdir('aa')) # 获取aa文件夹下所有的数据



# 8. rename(目标文件名，新文件名) -- 重命名文件夹 aa重命名为aaaa
os.rename('aa','aaaa')

# 12.9 小总结
 
# 文件操作小总结

'''
r文件指针在开头，能读取出来数据
w文件指针在开头，会把原内容覆盖掉
a文件指针在结尾，向右读取不出来数据，想要a模式能读取出来数据，用seek()改变文件指针位置

可以重命名文件也可以重命名文件夹
'''


"""
文件操作步骤
    打开：文件对象 = open(目标文件，访问模式)
    操作：
        1.读
          文件对象.read()
          文件对象.readlines()
          文件对象.readline()
        2.写
           文件对象.write()
           
    改变指针：seek()
    
    关闭: 文件对象.close
主访问模式
    w:写，文件不存在则新建该文件
    r:读，文件不存在则报错
    a:追加
文件和文件夹操作
    重命名：os.rename     可以重命名文件也可以重命名文件夹
    获取当前目录路径：os.getcwd()
    获取目录列表：os.listdir()
            
"""
