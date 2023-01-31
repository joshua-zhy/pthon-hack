# 9.9 递归函数和匿名函数（lambda）
 
# 递归函数的应用


# 递归函数：1.内部自己调用自己  2.必须有出口
# 递归是一种编程思想，函数是编程的一种体现
# return有两个作用: 1. 返回值 2. 退出当前函数

'''
需求：3以内数字累加和3 + 2 + 1 = 6
6 = 3 + 2以内数字累加和
2以内的累加和 = 2 + 1以内的累加和
1以内的累加和 = 1   # 出口
'''

def sum_numbers(num):
    # 2.出口
    if num == 1:
        return 1
    # 1. 当前数字 + 当前数字减一的累加和
    return num + sum_numbers(num - 1)

result = sum_numbers(3)
print(result)

# 如果没有出口，报错：超出最大递归深度

 
 
# 匿名函数lambda，来个栗子感受一下

'''
应用场景：
    1.lambda的作用就是简化代码
    2.如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化
语法：lambda 参数列表 ：表达式
注意：
    lambda表达式的参数可有可无，函数的参数在lambda表达式中完全适用
    lambda表达式能接收多个参数但只能返回一个表达式的值
'''

# 需求：函数 返回值100
# 1. 函数
# def fn1():
#     return 100
#
# result = fn1()
# print(result)


# 2. lambda 匿名函数,就是不在用def语句定义的函数。如果要声明匿名函数，则要使用lambda关键字
# lambda参数列表：表达式
fn2 = lambda : 100
print(fn2)   # lambda内存地址
# 100返回值 调用函数
print(fn2())   # 100
 
 
# lambda的参数形式

# 1.无参数
# fn1 = lambda: 100
# print(fn1())

# 2. 一个参数
# fn2 = lambda a: a
# print(fn2('hello world'))

# 3. 默认参数/缺省参数
# fn3 = lambda a, b, c = 200 : a + b + c
# print(fn3(10, 20))
# print(fn3(10, 20, 300))

# 4. 可变参数：*args
# fn4 = lambda *args: args
# print(fn4(10))
# print(fn4(10, 20))
# print(fn4(10,20,30,40))    # (10, 20, 30, 40)

# 5. 可变参数: **kwargs
fn5 = lambda **kwargs : kwargs
print(fn5(name = 'Python'))
print(fn5(name = 'Python', age = 30))   # {'name': 'Python', 'age': 30}


 
# 带判断的lambda

# lambda应用
# 1. lambda 两个数字比大小，谁大返回值

fn1 = lambda a, b : a if a > b else b
print(fn1(1000, 500))   # 1000
 
# 列表数据排序

'''
students是一个序列名，指代的就是列表序列，key等于一个 lambda的表达式，
这里面就用到了lambda，sort里面有个参数key，如果列表里面有字典，按照字典某个key进行排序用的。
将来要进行升或降序排序的数据，这里指得是字典，返回值，排序的依据是name key还是age key
里面形参x指代的是所有的字典，
'''
students = [
    {'name':'tom','age':20},
    {'name':'jock','age':21},
    {'name':'rose','age':22}
]

# 1. name key对应的值进行降序排序
students.sort(key=lambda x: x['name'])
print(students)
# 2. age key对应的值进行升序排序
students.sort(key=lambda x: x['age'])
print(students)
# 3. age key对应的值进行降序排序
students.sort(key=lambda x: x['age'],reverse=True)
print(students)

 

# lambda小总结

# '''
# 一、 lambda 
#    （1）语法
#         lambda 参数列表: 表达式
        
#     （2）lambda的参数形式
    
#         无参数:
#             lambda: 表达式
            
#         一个参数(多个参数用逗号隔开):
#             lambda 参数:表达式
            
#         默认参数:
#             lambda key=value:表达式
            
#         不定长位置参数:
#             lambda *args:表达式
            
#         不定长关键字参数:
#             lambda **kwargs:表达式
# '''