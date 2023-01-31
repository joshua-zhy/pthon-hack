# 9. Python函数
# Python函数的使用其实跟C、和Java函数的使用都是大同小异的。

# 函数的作用： 装代码，高效的代码重用

 

# 9.1 函数的使用
# 基本使用

# 1. 定义函数
def sel_func():
    print('I Love Python')

# 2. 函数调用
print('恭喜你登录成功')
sel_func()

'''
注意
	1. 不同的需求，参数可有可无
	2. 在Python中，函数必须先定义后使用
	3. 当调用函数的时候，解释器回到定义函数的地方去执行下方缩进的代码，当这些代码执行完，
	   回到调用函数的地方继续向下执行定义函数的时候，函数体内部缩进的代码并没有执行
'''

 
 
# 有参数的函数

# 函数的参数：函数调用的时候可以传入真实数据，增大函数的使用的灵活性
# 形参：函数定义时书写的参数（非真实数据）
# 实参：函数调用时书写的参数（真实数据）

# 参数形式传入真实数据，做加法运算
# 这里的a、b是形参
def add_num2(a,b):
    result = a + b
    print(result)

# 10，20是实参
add_num2(10,20)  # 输出30
 
 
# 函数中return的作用

def buy():
    return '烟'
    # print('ok')   #这一行代码不执行

goods = buy()
print(goods)

'''
return 作用：
			1. 负责函数返回值
			2. 退出当前函数：导致return下方的所有代码（函数体内部）不执行
'''
 

# 9.2 函数的说明文档
# 就是自己书写函数的时候，可以在函数里写一个说明文档，以后通过这个说明文档可以直接查看这个函数什么作用。

# len是内置函数，早在定义的时候就已经封装好说明文档了
# 自己写的函数没有说明文档，为了方便后期查看这种解释说明的信息更快捷更方便，定义函数的同时，定义一个说明文档就可以了
# 函数内部缩进的第一行书写的多行注释才是说明文档。如果敲了回车，则会更详细的显示（参数和返回值）。

help(len)  # help函数作用：查看函数的说明文档（函数解释说明的信息）
# def sum_num(a,b):
#     ''' 求和函数 '''  # 定义函数的说明文档
#     return a + b
# help(sum_num)

# 函数的说明文档的高级使用。 就是多行注释按回车，会出现参数1、2和renturn,说明他们的作用。
def sum_num1(a,b):
    '''
    求和函数sum_num1
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    '''
    return a + b
help(sum_num1)


# 9.3 函数的嵌套调用
# 来个栗子感受一下嵌套调用

# 所谓函数嵌套调用指的是一个函数里面有调用了另外一个函数

# 需求：两个函数testA 和 testB  ---- 在A里面嵌套调用B


def testB():
    print('B函数开始-----')
    print('这是B函数')
    print('B函数结束-----')

def testA():
    print('A函数开始')
    # 嵌套调用B
    testB()
    print('A函数结束')

testA()