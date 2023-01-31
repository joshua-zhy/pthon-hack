# 继承：子类默认继承父类的所有属性和方法

# 1. 定义父类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)

# 2. 定义子类 继承父类
class B(A):
    pass

# 3. 创建对象，验证结论
result = B()
result.info_print()

'''
再python中，所有类默认继承object类，object类是顶级类或基类其他子类叫做派生类
'''
# 1. 师傅类 属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
# 2. 定义徒弟类，继承师傅类
class Prentice(Master):
    pass

# 3. 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()



# 多继承

# 1. 师傅类 属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承，添加School父类
class School(object):
    def __init__(self):
        self.kongfu = '[哈哈煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2. 定义徒弟类，继承师傅类
class Prentice( School,Master):
    pass

# 3. 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

'''
多继承就是一个类同时继承多个父类
结论：如果一个类继承多个符类，优先继承第一个父类的同名属性和方法
'''