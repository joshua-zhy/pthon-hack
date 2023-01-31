# .3 容器类型转换
 
# 直接上栗子：

# 已有的数据类型和程序想要的数据类型不一样，这个时候利用函数做类型的转换就可以了。

list1 = [10,20,30]
s1 = {100, 200, 300}
t1 = ('a', 'b', 'c')

# tuple():将某个序列转换成元组
print(tuple(list1))  # 输出结果为(10, 20, 30)
print(tuple(s1))    # 输出结果为(200, 100, 300)

# list():转换成列表
print(list(s1))      # 输出结果为 [200, 100, 300]
print(list(t1))     # 输出结果为 ['a', 'b', 'c']

# set():转换成集合
print(set(list1))   # 输出结果为{10, 20, 30}
print(set(t1))      # 输出结果为{'c', 'b', 'a'}

'''
注意：
    1. 集合可以快速完成列表去重
    # 2. 集合不支持下标（因为没有顺序）
    
'''