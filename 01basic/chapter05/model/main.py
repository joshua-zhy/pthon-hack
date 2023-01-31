'''
再python程序当中，每个模块就是一个python文件，这个python文件都有自己的名字。
name是一个系统变量，是模块的标识符，是每个python文件的标识符，如果name的使用位置再在自身模块里
那么它的值就是__main__,否则不在自身模块里面，那么这个name的值就是我们模块的名字，即是我们的python文件名。
'''
# 1. 导入模块
import my_module1

# 2. 调用功能
my_module1.testA(2,2)

'''

当导入一个模块，Python解析器对模块的搜索顺序是：
1. 当前目录
2. 如果不在当前目录，Python则搜索shell变量PYTHONPATH下的每个目录（安装解释器目录下的）
3. 如果都找不到，Python会查看默认路径。UNIX下，默认路径一般为/usr/local/lib/python（一般不涉及到默认路径）

模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录

注意：
    自己的文件名不要和已有的模块名重复，否则导致模块功能无法使用
    使用from 模块名 import 功能的时候，如果功能名字重复，调用到的是最后定义或导入的功能
'''

# 1. 自己的模块名不能和已有的模块名重复
import random
num = random.randint(1,5)  # 因为在当前目录中有一个random模块，则报错
print(num)




















