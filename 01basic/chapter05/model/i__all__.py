'''
如果一个模块文件中有__all__变量，当使用from xxx import * 导入时，只能导入这个列表中的元素
'''
from my_module2 import *

testA()

# 因为testB函数没有添加all列表，只有all列表里面的功能才能导入
# testB()
