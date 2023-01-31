# 14.2.4 super()方法
'''
super方法的作用是调用父类方法用的，有参数写法，有无参写法。
无参写法最简单直观。
使用super()可以自动查找父类。调用顺序遵循_mro_类属性的顺序。比较适合单继承使用。
'''
# 1. 师傅类 属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承，添加School父类
class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        # 2.1 super()带参数写法
        # super(School,self).__init__()
        # super(School,self).make_cake()

        # 2.2 无参数super()
        super().__init__()
        super().make_cake()



# 2. 定义徒弟类，继承师傅类 和 学校类， 添加和父类同名的属性和方法
class Prentice( School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'
    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 调用父类的同名方法和属性，把父类的同名属性和方法再次封装
    # 调用父类方法，但是为保证调用到的也是父类的属性，必须在调用方法前调用父类的初始化
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    # 子类调用父类的同名方法和属性：把父类的同名属性和方法再次封装
    def make_old_cake(self):
        # 方法一：如果定义的类名修改，麻烦。代码量庞大，冗余。
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)

        # 方法二: super()
        # 2.1 super(当前类名，self).函数()
        # super(Prentice,self).__init__()
        # super(Prentice,self).make_cake()

        # 2.2 无参数的super()
        super().__init__()
        super().make_cake()


daqiu = Prentice()
daqiu.make_old_cake()
