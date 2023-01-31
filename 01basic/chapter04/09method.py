# 14.4.1 类属性
 
# 下面就是类属性

class Dog(object):
    # 类属性
    tooth = 10
 
# 设置和访问类属性

'''
类属性就是类对象所拥有的属性，它被该类的所有实例对象所共有。
类属性可以使用类对象或实例对象访问
'''
# 1. 定义类，定义类属性
class Dog(object):
    # 类属性
    tooth = 10

# 2. 创建对象
wangcai = Dog()
xiaohei = Dog()

# 3. 访问类属性：类和对象
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

'''
类属性的优点
    1. 记录的某项数据 始终保持一致，则定义类属性
    2. 实例属性 要求每个对象为其单独开辟一份内存空间来记录数据，而类属性为全类所共有，仅占一份内存，更加节省内存空间
    
'''

1
 
# 修改类属性

'''
类属性只能通过类对象修改，不能通过实例对象修改，如果通过实例对象修改类属性，表示的是创建了一个实例属性
'''

class Dog(object):
    tooth = 10

wangcai = Dog()
xiaohei = Dog()

# 1. 类 类.类属性 = 值
# Dog.tooth = 20
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)

# 2. 测试通过对象修改类属性
wangcai.tooth = 200
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)



# 14.4.2 实例属性
def __init__(self):
	# 实例属性
	self.age = 1
# 14.5 类方法和静态方法
# 14.5.1 类方法
'''
类方法特点：
    需要用装饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数

类方法使用场景:
    1. 当方法中 需要使用类对象（如访问私有类属性等）时，定义类方法
    2. 类方法一般和类属性配合使用
'''

# 1. 定义类：私有类属性，类方法获取这个私有类属性
class Dog(object):
    __tooth = 10

    # 定义类属性
    @classmethod
    def get_tooth(cls):    # cls代表Dog这个类
        return cls.__tooth

# 2. 创建对象(通过)
wangcai = Dog()
result = wangcai.get_tooth()
print(result)

# 也可以直接通过类名调用类方法
result1 = Dog.get_tooth()
print(result1)

 

# 14.5.2 静态方法
'''
静态方法的特点：
    需要通过修饰器@staticmethod来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）
    静态方法也能够通过实例对象和类对象去访问

静态方法使用场景：
    1. 当方法中既不需要使用实例对象（如实例方法，实例属性），也不需要使用类对象（如类属性、类方法、创建实例等）时，
    定义静态方法
    2. 取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
'''
# 1. 定义类，定义静态方法
class Dog():
    @staticmethod
    def info_print():
        print("这是一个静态方法")

# 2. 创建对象
wangcai = Dog()

# 3. 调用静态方法：类 和 对象
wangcai.info_print()
Dog.info_print()
