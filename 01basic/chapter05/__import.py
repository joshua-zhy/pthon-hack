'''
# 包将有联系的模块组织在一起，即放到同一个文件夹下，并且在这个文件夹创建一个名字为__init__.py文件，那么这个文件就称为包
# 当右键去创建包的时候，这个文件夹里面会自动创建一个名字为__init__.py的文件，这个文件可以控制包的导入行为

'''

# 方法一
'''
1. 导入
import 包名.模块名
2. 调用功能
包名.模块名.功能（）
'''
# 导入mypackage包下的模块1，使用这个模块内的info_print1函数
# import mypackage.my_module1
# mypackage.my_module1.info_print()


# 方法二：注意 设置__init__.py文件里面的all列表( __all__ = [] )，添加的是允许导入的模块
'''
from 包名 import *
模块名.目标
'''
from mypackage import *
my_module1.info_print()

# 每个python模块（python文件，也就是此处的 test.py 和 import_test.py）都包含内置的变量 __name__，当该模块被直接执行的时候，__name__ 等于文件名（包含后缀 .py ）；如果该模块 import 到其他模块中，
# 则该模块的 __name__ 等于模块名称（不包含后缀.py）。



# 在工作岗位下，避免功能名字重复这个事情发生

# 1. 当使用from xx  import 功能
# 导入模块功能的时候，如果功能名字重复，导入的时候后定义或后导入的这个同名功能

def sleep():
    print('我是自定义的sleep')

from time import sleep

# 后导入的同名功能（这时就会报错）
# def sleep():
#     print('我是自定义的sleep')
sleep(2)



# 2. 拓展：名字重复
# 问题：import 模块名 时候担心名字重复的问题-不需要（因为功能名一样但是模块名不一样）
import time
print(time)

time = 1   # 这个变量会覆盖模块的功能
print(time)

# 问题：为什么变量也能覆盖模块？-- 在Python语言中，数据是通过 引用 传递的