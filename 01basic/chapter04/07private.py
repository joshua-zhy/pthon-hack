# 14.2.5 获取和修改私有属性
 
# 私有权限

'''
设置私有权限的方法：在属性名和方法名前面加上两个下划线__
'''
# 1. 师傅类 属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承，添加School父类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2. 定义徒弟类，继承师傅类 和 学校类， 添加和父类同名的属性和方法
class Prentice( School,Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'
        # self.money = 3000000
        # 添加私有属性
        self.__money = 3000000

    # 定义私有方法
    def __info_print(self):
        print("这是一个私有方法")

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')



# 步骤：1. 创建Tusun，用这个类创建对象   2.用这个对象调用父类的属性或方法
class Tusun(Prentice):
    pass

xiaoqiu = Tusun()
# print(xiaoqiu.money)  # 添加了私有属性之后就不能访问了
# xiaoqiu.info_print()   # 添加了私有方法之后就不访问了

 
# 获取和修改私有属性

'''
私有属性和私有方法只能在类里面访问和修改。
在Python中，一般定义函数名get.xx用来获取私有属性，定义set_xx用来修改私有属性值
get_xx、set_xx函数名可以是其他的名，使用他们只是工作习惯
'''
# 1. 师傅类 属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承，添加School父类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2. 定义徒弟类，继承师傅类 和 学校类， 添加和父类同名的属性和方法
class Prentice( School,Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'
        # self.money = 3000000
        # 添加私有属性
        self.__money = 3000000

    # 定义函数：获取私有属性值 get_xx
    def get_money(self):
        return self.__money
    # 定义函数：修改私有属性值 set_xx
    def set_money(self):
        self.__money = 999999

    # 定义私有方法
    def __info_print(self):
        print("这是一个私有方法")

    def make_cake(self):
        # 如果事先调用了父类的属性和方法，父类属性会覆盖子类属性，所以在调用子类属性前调用父类的初始化
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')


# 步骤：1. 创建Tusun，用这个类创建对象   2.用这个对象调用父类的属性或方法
class Tusun(Prentice):
    pass

xiaoqiu = Tusun()
# print(xiaoqiu.money)  # 添加了私有属性之后就不能访问了
# xiaoqiu.info_print()   # 添加了私有方法之后就不访问了
print(xiaoqiu.get_money())    # 3000000
xiaoqiu.set_money()
print(xiaoqiu.get_money())   # 999999

# 4.2.6 继承小总结

'''
继承的特点：
    子类默认拥有父类的所有属性和方法
    子类重写父类同名方法和属性
    子类调用父类同名方法和属性
super()方法快速调用父类方法

私有权限：
    不能继承给子类的属性和方法需要添加私有权限
    语法
class 类名():
    # 私有属性
    __属性名 = 值

    # 私有方法
    def __函数名(self)
        代码

在类的里面可以要获取私有属性get_xx
修改私有属性set_xx
'''