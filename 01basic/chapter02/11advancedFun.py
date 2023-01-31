# 11. 高级函数
 
# 高阶函数作用： 为了化简代码，增加函数的灵活性
 

# 11.1 abs()和round()函数
# 这两个函数的用法比较简单，来个栗子就会了。but这两个函数不是高阶函数


# abs() 求绝对值用的
print(abs(-10))  # 10


# round()  四舍五入的计算
print(round(1.2))  # 1
print(round(1.6))  # 2

# abs()和round()不是高阶函数

 

# 11.2 内置高阶函数（map、reduce、filter）
 
# 先来体验一下高阶函数

# 需求: 任意两个数字，先进行数字处理（绝对值或四舍五入）在求和运算

# 1. 写法一
def add_num(a,b):
    # 绝对值
    return abs(a) + abs(b)

result = add_num(-1.1, 1.0)
print(result)    # 2.1

# 2. 写法二
def sum_num(a, b, f):
    return f(a) + f(b)

result1 = sum_num(-1,-2,abs)
print(result1)  # 3

result2 = sum_num(1.2, 1.4, round)
print(result2)  # 2

# 方法二的代码更加简洁，函数灵活性较快
# 函数式编程大量使用函数，减少了代码的重复，因此程序比较短，开发速度较快
'''
高阶函数：把函数作为参数传入，这样的函数称为高阶函数，高阶函数是函数式编程的体现。函数式编程就是指这种高度抽象的编程范式。
高阶函数其实作用就是为了化简代码，增加函数的灵活性
'''
 
 
map()#函数

'''
map(func, lst),将传入的函数变量func作用到lst变量的每个元素中,并将结果组成新的列表(Python2)/
迭代器(Python3)返回
'''

# 1. 准备列表数据
list1 = [1, 2, 3, 4, 5]

# 2. 准备2次方计算的函数
def func(x):
    return x ** 2

# 3. 调用map
result = map(func, list1)

# 4. 验收成果
# 在打印迭代器的时候,只能返回内存地址,这时要用list()转换数据类型
print(result)     # 输出 <map object at 0x00000208211131D0>
print(list(result))  # [1, 4, 9, 16, 25]


 
# reduce函数

'''
reduce(func, lst),其中func必须有两个参数. 每次func计算的结果继续和序列的下一个元素作累计计算.
注意: reduce()传入的参数func必须接收2个参数
'''

list1 = [1, 2, 3, 4, 5]
# 1. 导入模块
import functools

# 2.定义功能模块
def func(a, b):
    return a + b

# 3. 调用reduce. 作用:功能函数计算的结果和序列的下一个数据作累计计算
result = functools.reduce(func, list1)
print(result)    # 输出结果为 15    

 
filter()#函数

'''
filter(func, lst)函数用于过滤序列,过滤掉不符合条件的元素,返回一个filter对象. 如果要转换为列表,可以使用list()来转换
'''
list1 = [1,2,3,4,5,6,7,8,9,10]

# 1. 定义功能函数:过滤序列中的偶数
def func(x):
    return x % 2 == 0

# 2. 调用filter
result = filter(func,list1)
print(result)       # <filter object at 0x000002AEA49031D0>
print(list(result))      # [2, 4, 6, 8, 10]