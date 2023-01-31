# 6. Python模块
 

# 16.1 模块的基本使用
 

# 模块就是一个python文件，直接调用这个模块里的功能，省去了自己定义功能再使用的步骤。
# 不推荐一次性导入多个模块，推荐的是跟一个模块名

# 需求：math模块下sqrt（）开平方计算

# 方法一：import 模块名     模块名.功能
import math
print(math.sqrt(9))  # 3.0
# 再python当中，涉及到类似于除法计算不管参与计算的数字是否有浮点数，将来反馈回来的结果一定是浮点数。

# 方法二：from 模块名 import 功能1，功能2...    直接功能调用
from math import sqrt
print(sqrt(9))

# 方法三：from math import *      直接功能调用
from math import *
print(sqrt(9))  

# 定义别名

# 需求：运行后暂停2秒打印hello
'''
1. 导入time模块或导入time模块的sleep功能
2. 调用功能
3. 打印hello
'''

# 1.  模块别名    注意：如果定义了别名之后就只能使用别名
# import time as tt
# tt.sleep(2)
# print('hello')

# 2. 定义别名
from time import sleep as sl
sl(2)
print('hello')