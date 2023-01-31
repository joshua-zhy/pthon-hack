# 13. Python面向对象（上）
# 13.1 类和对象
# 需求：洗衣服   功能：能洗衣服
# 1. 定义洗衣机类
'''
class 类名():
    代码
'''

class Washer():
    def wash(self):     # 这里的self指的是调用该函数的对象
        print("能洗衣服")

# 2. 创建对象
# 对象名 = 类名()
haier = Washer()

# 3. 验证成果
# 打印haier对象
print(haier)   # 输出的是地址值

# 使用wash功能 -- 实例方法/对象方法 -- 对象名wash()
haier.wash()


# 1. 一个类可以创建多个对象 2. 多个对象都调用函数的时候，self地址是不相同的

haier1 = Washer()
haier1.wash()

haier2 = Washer()
haier2.wash()



# =====================================================
class Washer():
    def wash(self):
        print('洗衣服')

haier1 = Washer()

# 添加属性 对象名.属性名 = 值
haier1.width = 400
haier1.height = 500

# 获取属性 对象名.属性名
print(f'洗衣机的宽度是{haier1.width}')
print(f'洗衣机的高度是{haier1.height}')



# 类里面获取对象属性

class Washer():
    def wash(self):
        print('洗衣服')

    def print_info(self):
        # self.属性名
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

haier1 = Washer()

# 添加属性 对象名.属性名 = 值
haier1.width = 400
haier1.height = 500

# 对象调用方法
haier1.print_info()

 

# 13.1.2 魔方方法（__init__、__str__、__del__）
# 魔法函数是具有特殊功能的函数

# __init__魔法方法

# _init_()方法的作用：初始化对象
class Washer():
    def __init__(self):
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

haier = Washer()

haier.print_info()

'''
1. _init_()方法，再创建一个对象时默认被调用，不需要手动调用
2. _init_(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递过去
'''



# 带参数的__init__魔法方法

# 1. 定义类：带参数的init：宽度和高度   作用：创建多个对象且属性值不同
# 实例方法：调用实例属性
class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def print_info(self):
        print(f'洗衣机的宽度是{self.width},洗衣机的高度是{self.height}')

# 2.  创建对象，创建多个对象且属性值不同：调用实例方法
haier = Washer(10,20)
haier.print_info()

haier2 = Washer(100, 200)
haier2.print_info()


# __str__魔法方法

class Washer():
    def __init__(self):
        self.width = 300

    def __str__(self):
        return '解释说明：类的说明或对象状态的说明'

haier = Washer()
print(haier)

'''
作用说明：当使用print输出对象的时候，默认打印出现的内存地址。如果类定义了_str_方法，
那么就会打印从这个方法中return的数据
'''

# _def__魔法方法

'''
del haier1,不去手动删除对象也能调用del魔法方法，这几行代码执行完之后，内存中存储的函数、类、变量也会自动释放内存，
即对象也会被删除掉，所以del魔法方法也是被自动调用的。
'''
class Washer():
    def __init__(self):
        self.width = 300

    def __del__(self):
        print('对象已经删除')

haier = Washer()

# del haier   当删除对象时，python解释器也会默认调用__del__()方法