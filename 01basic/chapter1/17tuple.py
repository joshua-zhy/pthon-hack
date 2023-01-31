# 输出元组
t1 = (10, 20, 30)
print(t1)  # 输出 (10, 20, 30)

# 如果是单个数据的元组，那么后面必须加逗号，否则就不是元组的数据类型，而是整个数据本身的数据类型
# 1.多个数据元组
t1 = (10, 20, 30)
print(type(t1))  # 输出 <class 'tuple'>

# 2. 单个数据元组
t2 = (10,)
print(type(t2))  # 输出 <class 'tuple'>

# 3. 如果单个数据的元组不加逗号
t3 = (10)
print(type(t3))  # 输出 <class 'int'>

t4 = ('aaa')
print(type(t4))  # 输出 <class 'str'>
t5 = ('aaa',)
print(type(t5))  # 输出  <class 'tuple'>
