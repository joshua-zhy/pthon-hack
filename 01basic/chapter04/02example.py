# 13.1.3 举两个栗子（烤地瓜、搬家具）
# 烤地瓜

# 1. 定义类：初始化属性、被烤和添加调料的方法，显示对象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 烤的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []
    def cook(self, time):
        '''烤地瓜方法'''
        # 1. 先计算地瓜整体烤过的时间
        self.cook_time += time
        # 2. 用整体烤过的时间判断地瓜的状态
        if 0 <= self.cook_time < 3 :
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5 :
            self.cook_state = '半生不熟的'
        elif 5 <= self.cook_time < 8 :
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            self.cook_state = '烤糊了'

    def add_condiments(self,condiment):
        # 用户意愿的调料追加到调料列表
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜的被烤过的时间是{self.cook_time},状态是{self.cook_state},调料有{self.condiments}'

# 2. 创建对象并调用对应的实例方法
digua1 = SweetPotato()
print(digua1)

digua1.cook(2)
digua1.add_condiments('辣椒面儿')
print(digua1)

digua1.cook(4)
digua1.add_condiments('酱油')
print(digua1)



# 搬家具

class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area

class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

