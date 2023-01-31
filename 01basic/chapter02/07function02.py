# 9.4 变量的作用域
# 局部访问

# 定义一个函数，声明一个变量：函数体内部访问，函数体外部访问
def testA():
    a = 100
    print(a)  # 函数体内部访问，能访问到a变量

testA()
print(a) # 报错：a变量是函数内部的变量，函数外部无法访问，这里的a是一个局部变量

 
 
# 访问全局变量

# 声明全局变量：函数体内外都能访问
a = 100 
print(a)

def testA():
    print(a)

def testB():
    print(a)

testA()
testB()

 
 
# 修改全局变量

# 函数体内修改全局变量

a = 100
print(a)  # 输出100

def testA():
    print(a)

def testB():
    global a
    a = 200
    print(a)

testA()     # 输出100
testB()     # 输出200
print(a)    # 输出200
'''
总结：
    1. 如果在函数里面直接把变量a = 200赋值，此时的a不是全局变量的修改，而是相当于在函数内部声明了一个新的局部变量
    2. 函数体内部修改全局变量：先global声明a为全局变量，然后再变量重新赋值
'''

1


# 多函数执行流程

# 1.声明全局变量 2. 定义两个函数 3.函数1修改全局变量：函数2访问全局变量
glo_num = 0

def test1():
    global glo_num
    glo_num = 100

def test2():
    print(glo_num)


 # 疑问：已经再test1中修改了全局变量，为什么这个地方输出结果不是100？因为进行函数调用，没有执行函数体内的代码。
print(glo_num)  # 输出结果为0
test2()  # 输出的结果为0。还是因为因该全局变量的函数没有执行

test1()  # 执行了函数体内的代码
test2()  # 输出100
print(glo_num)  # 输出100，因为test1函数调用了，修改了全局变量。


 
 

# 9.5 函数返回值（多返回值）
 
# 返回值作为参数传递


def test1():
    return 50

def test2(num):
    print(num)

# 先得到函数1的返回值，再把这个返回值传入到函数2
result = test1()
test2(result)


 
 
# 函数的返回值（多返回值）

# 需求：一个函数有两个返回值1和2
# 一个如果有多个return不能都执行，只执行第一个return：无法做到一个函数多个返回值

# def return_num():
#     return 1
#     return 2
#
# result = return_num()
# print(result)  # 输出结果为1。第二个return不起作用

'''
1. 下面是一个函数多个返回值的正确写法
2. return a,b写法，返回多个数据的时候，默认是元组类型
3. return后面可以连接列表、元组或字典，以返回多个值
'''

def return_num():
    return 1,2   # 返回值是元组
    # return 后面可以直接写元组、列表、字典、返回多个值.
    # return (10,20)  # 返回的是元组
    # return [100,200]  # 返回的是列表
    # return {'name':'Python', 'age': 20} # 返回的是字典
result = return_num()
print(result)  # return 1,2 输出结果是(1, 2)

 

# 9.6 函数的参数的类型
 
# 位置参数

def user_info(name,age,gender):
    print(f'您的姓名是{name},年龄是{age}，性别是{gender}')

user_info('tom',20,'男') # 输出结果为 您的姓名是tom,年龄是20，性别是男

# 注意：传递和定义参数的顺序及个数必须一致
# user_info('tom',20) # 个数定义和传入不一致会报错
# user_info(20,'tom','男')  # 顺序也和定义必须是一致的，否则倒是数据无意义
 
 
# 关键字参数

# 函数调用，通过"键=值"形式加以指定
def user_info(name,age,gender):
    print(f'您的姓名是{name},年龄是{age}，性别是{gender}')

# 1. 调用函数传参
user_info('jack', age=20 , gender='男')   # 您的姓名是jack,年龄是20，性别是男

# 2. 关键字参数之间部分先后循序
user_info('jack', gender='男', age=20)   # 您的姓名是jack,年龄是20，性别是男

# 3. 位置参数必须写在关键字参数的前面
# user_info(age=20 , gender='男', 'jack')  # 报错了。必须关键词放在前面
 
 
# 缺省参数

'''
1.缺省参数（默认参数）：为了节省用户的时间成本，提高用户体验，可以把一些需求上带有默认值的这种参数，设置成一个默认值，这样写法的参数，叫做缺省参数（默认参数）。
2. 所有的位置参数必须出现在默认参数的前面
3. 函数调用时，如果为缺省参数传值则修改默认参数值；否则使用这个默认值
'''

def user_info(name,age,gender='男'):    # gender='男'是缺省参数
    print(f'您的姓名是{name},年龄是{age}，性别是{gender}')

# 没有为缺省参数传值，表示使用默认值
user_info('tom', 18)  # 您的姓名是tom,年龄是18，性别是男

# 为缺省参数传值，使用了gender='女 '，即修改了默认值
user_info('tom', 18, gender='女') # 您的姓名是tom,年龄是18，性别是女

 
 
# 不定长参数之位置参数

'''
1.不定长参数也叫可变参数。用于不确定调用的时候会传递多少个参数（不传也可以）的场景。
  此时可以用包裹位置参数或者包裹关键字参数，来进行参数传递。
2. 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组，args是元组类型，这就是包裹位置传递
'''

# 接收所有位置参数，返回一个元组
def user_info(*args):
    print(args)

# 包裹位置传递
# 如果是*args接收不定长的位置参数据，可以传数据，也可以不传数据，无论传与不传，将来接收的都是所有位置参数，返回的是都是一个元组
user_info()              #  ()
user_info('tom')        #  ('tom',)
user_info('tom', 20)     #  ('tom', 20)
user_info('tom', 20,'男')  #  ('tom', 20, '男')

 
 
# 不定长参数之关键字参数

# 收集所有关键字参数，返回一个字典
# 包裹关键字传递
def user_info(**kwargs):
    print(kwargs)

user_info()
user_info(name='tom')
user_info(name='tom', age=20)

# 无论是包裹位置传递还是包裹关键字传递，都是一个组包的过程



# 扩展1：拆包

# 上面说了不定长参数是组包的过程，那就来说一下拆包的过程


# 1. 拆包元组数据
# def return_num():
#     return 100, 200

# result = return_num()
# print(result)    # 输出 (100, 200)

# num1, num2 = return_num()
# print(num1)   # 输出 100
# print(num2)   # 输出 200

# 2. 字典数据拆包：变量存储的数据是key值
# 先准备字典，然后拆包
dict1 = {'name': 'tom', 'age': 20}
# dict1中有两个键值对，拆包的时候用两个变量接收数据
a , b = dict1
print(a)     # 输出name
print(b)     # 输出age

# 提取value的值
print(dict1[a])     # 输出tom
print(dict1[b])     # 输出20
print(dict1['name'])  # 输出tom

