# 7.2 公共方法
# 公共方法之len()、del()、max()、min()、range(start,end,step)、enumerate()
# 个函数的作用以及用法，举栗子说明
 

# （1）len()：计算容器中元素的个数

str1 = 'abcd'
list1 = [10, 20, 30]
t1 = (100, 200, 300)
dict1 = {'name':'Python', 'age':30}
s1 = {10 , 20}

# len() 计算容器中元素个数
print(len(str1))  # 输出4
print(len(list1)) # 输出3
print(len(t1))    # 输出3
print(len(dict1)) # 输出2
print(len(s1))    # 输出2

# （2）del()：删除

str1 = 'abcd'
list1 = [10, 20, 30]
t1 = (100, 200, 300)
dict1 = {'name':'Python', 'age':30}
s1 = {10 , 20}

# 1. del 目标 或者 del(目标)

# str1字符串
del str1      # 删除整个字符串
print(str1)   # 报错说明已经删除成功

# ============================================================================
# list1 列表
del(list1)
print(list1) # 报错说明已经删除成功

# del(list1[0])
# print(list1)  # 输出[20, 30]

# del list1[0]
# print(list1)   # 输出[20, 30]

# ==============================================================================

# dict1 字典
del dict1
print(dict1) # 报错，已经删除成功
del dict1['name']
print(dict1)   #  输出结果为 {'age': 30}

# ==============================================================================

# s1 集合
del s1
print(s1) # 报错，已经删除成功

 
# （3） max()：返回容器中元素最大值
        #   min()：返回容器中元素最小值

str1 = 'abcde'
list1 = [10, 20, 30]

# 1. max()最大值
print(max(str1))  # 输出e
print(max(list1))  # 输出30

# 2. min():最小值
print(min(str1))  # 输出a
print(min(list1)) # 输出10
 
 
# （4）range()：生成从start到end的数字，步长为step，供for循环使用

"""
注意事项：
    1. 如果不写开始，默认从0开始
    2. 如果不写步长，默认为1
"""

print(range(1,10,1)) # 输出 range(1, 10)，返回的是可迭代的对象，需要配合for循环才能拿到数字
for i in range(1,10,1):
    # 遍历可迭代对象，并且拿到了对象内部的这些数字
    print(i)       # 输出的是1，2，3，4，5，6，7，8，9

for i in range(1,10):
    print(i)        # 如果不写步长，则默认步长是1

for i in range(1,10,2):
    print(i)       # 因为步长是2，所以输出1，3，5，7，9

for i in range(10):
    print(i)      # 这里的10代表结束。开始不写，默认从0开始。步长不写，默认为1。 但是不能不写结束！

 
# （5）enumerate()：函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，一般用于在for循环当中。

# 1. 语法： enumerate(可遍历对象，start = 0)
# 2. start参数用来设置遍历数据的下标的起始值，默认为0

list1 = ['a', 'b', 'c', 'd', 'e']
# enumerate 返回结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个数据是原迭代对象的数据
for i in enumerate(list1):
	print(i)
'''
输出的结果为：
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
'''

for i in enumerate(list1,start = 1):
    print(i)
'''
这时的start为1，输出的结果为：
(1, 'a')
(2, 'b')
(3, 'c')
(4, 'd')
(5, 'e')
'''