# 需求：尝试执行打印num，捕获异常类型NameError. 如果捕获到这个异常类型，执行打印，'有错误'
try:
    print(num)    # 可能发生的错误
except NameError:  # 异常类型
    print('有错误')   # 如果捕获到该异常类型执行的代码

'''
注意：
    1. 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。
    2. 一般try下方只放一行尝试执行的代码
'''

# 尝试执行的代码，并不能断定它的异常类型具体是什么，在except后用元组的方式，把可能的异常类型全都书写里面
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('有错误')

# 尝试执行的代码，并不能断定它的异常类型具体是什么，在except后用元组的方式，把可能的异常类型全都书写里面
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('有错误')
# 尝试执行打印num， 捕获Exception 打印异常描述信息


try:
    print(num)
except Exception as result:
    print(result)
    
# Exception是所有程序异常类的父类
# 不需要程序员指定具体的异常类型
# 捕获所有异常就是去except捕获这个Exception，从而做到捕获了父类，即捕获到了具体的某个异常类

# 15.2.5 else和finally
 

# else


'''
else表示的是如果没有异常要执行的代码
'''
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('我是else，当没有异常的时候执行的代码')
# finally

# 需求：尝试以r打开文件，如果有异常以w打开这个文件，最终关闭文件
'''
finally表示的是无论是否异常都要执行的代码，例如关闭文件
'''
try:
    f = open('test300.txt','r')
except Exception as e:
    print(e)
    f = open('test300.txt','w')

finally:
    f.close()

# 15.3 异常的传递
 

'''
# 异常的传递指代的就是我们的异常是可以嵌套书写的，要去了解嵌套书写异常语句的时候，
    我们的程序执行流程是什么.
# 这些要学习的知识点简称为异常的传递
# 如果书写打开访问模式，不写访问模式，那么默认即为只读r模式
# 先执行外层的try、except，然后在执行内层的try、except
'''

'''
需求1：尝试只读打开test.txt 文件存在读取内容，不存在提示用户
需求2：读取内容：循环读取，当无内容的时候退出循环，如果用户意外终止，提示用户已经意外终止
'''
import time
try:
    f = open('test.txt')
    # 尝试循环读取内容
    try:
        while True:
            con = f.readline()
            # 如果读取完成退出循环
            if len(con) == 0:
                break
            time.sleep(3)
            print(con)
    except:
        # 在命令提示符中如果按下ctrl+c结束符终止的键
        print('程序被意外终止')
except:
    print('该文件不存在')



# 15.4 自定义异常
 

'''
自定义异常的作用：用来我们将不满足程序逻辑的情况，进行一个反馈，报错给用户。
用来报错，报的错误不是语法错误，而是不符合我们程序逻辑要求的错误。
'''

# 1.定义异常类，继承Exception 魔法方法有init和str(设置异常描述信息)
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        # 用户输入的密码长度
        self.length = length
        # 系统要求的最少长度

        self.min_len = min_len

    # 设置异常描述信息
    def __str__(self):
        return f'您输入的密码长度是{self.length},密码不能少于{self.min_len}'

def main():
    # 2. 抛出异常：尝试执行：用户输入密码，如果长度小于3，抛出异常
    try:
        password = input('请输入密码：')
        if len(password) < 3:
            # 抛出异常类创建的对象
            # ShortInputError(len(password),3)抛出了一个对象而已。可以理解raise相当于原来的打印。打印对象的时候，打印到的就是str魔法对象的返回值。
            # raise抛出这个对象的时候，我们捕获的时候，捕获到的也是str魔法方法的返回值
            raise ShortInputError(len(password),3)
    # 3. 捕获该异常
    except Exception as result:
        print(result)

    else:
        print('没有异常，密码输入完成')

main()


 
 

# 15.5 小总结
 

'''
1. 异常语法

try：
    可能发生的异常
except:
    如果出现异常执行的代码
else：
    没有异常执行的代码
finally：
    无论是否异常都要执行的代码

2. 捕获异常

except 异常类型：
    代码
except 异常类型 as xx：
    代码

3. 自定义异常

# 1.自定义异常类
class 异常类类名(Except):
    代码

    # 设置抛出异常的描述信息
    def __str__(str):
        return ...

# 2. 抛出异常
raise 异常类名()

# 捕获异常
except Exception...
'''

