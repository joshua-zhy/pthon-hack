# 14.2.1 子类重写与调用父类同名属性和方法
 
# 子类重写父类同名属性和方法

# 1. 师傅类 属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承，添加School父类
class School(object):
    def __init__(self):
        self.kongfu = '[学校煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2. 定义徒弟类，继承师傅类 和 学校类， 添加和父类同名的属性和方法
class Prentice( School,Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 3. 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

'''
结论：如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法的时候，
调用到的是子类里面的同名属性和方法。这个现象在python语言里当中，简称之为子类重写父类同名方法和属性
'''

# 14.2.3 小拓展（__mro__）
'''
如果要查看某个类的父类继承关系， 类.__mro__ 进行查看
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

print(Prentice.__mro__)   # (<class '__main__.Prentice'>, <class '__main__.Master'>, <class 'object'>)

