# 10. 学生管理系统
# 定义功能界面
def info_print():
    print('请选择功能------------------')
    print('1. 添加学生')
    print('2. 删除学生')
    print('3. 修改学生')
    print('4. 查询学生')
    print('5. 显示所有学生')
    print('6. 退出系统')
    print('-' * 20)

info = []
# 所有的功能函数都是操作学生信息，所有存储所有学生信息应该是一个全局变量，数据类型为列表。


#  添加学生信息的函数
def add_info():
    """添加学生函数"""     # 添加函数的说明文档
    pass                 # 当我们还不知道函数体内部要写什么代码的时候，加一个pass作占位，，避免语法出现错误。
    # 1.用户输入：学号、姓名、手机号
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')

    # 2. 判断是否添加这个学生，如果学生姓名已经存在报错提示；如果姓名不存在则添加数据
    global info

    # 2.1 不允许姓名重复：判断用户输入的姓名 和 列表里面字典的name对应的值相等，提示
    for i in info:
        if new_name == i['name']:
            print('此用户已经存在')
            # return作用：退出当前函数：准备空字典，字典新增数据，列表追加字典
            return

    # 2.2 如果输入的姓名不存在，添加数据：准备空字典，字典新增数据，列表追加数据
    info_dict = {}

    # 字典新增数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    # print(info_dict)

    # 列表追加字典
    info.append(info_dict)
    print(info)


# 删除学生
def del_info():
    """删除学生"""
    del_name = input('请输入要删除学生的姓名：')
    global info   # 声明全局变量
    for i in info:      # 遍历列表
        if del_name == i['name'] :
            # 如果姓名存在，则在列表删除数据
            info.remove(i)
            break
    else:        # else的作用：当循环正常结束要执行的代码。就是遍历完列表中的数据，还没有break。
        print('该学员不存在！！！')
    print(info)



# 修改函数
def modify_info():
    """修改学生信息"""
    modify_name = input('请输入要修改的学生的姓名：')
    global info
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入新的手机号：')
            break
    else:
        print('该学生不存在！！！')
    # 打印info
    print(info)


# 查询学员信息
def search_info():
    """查询学生信息"""
    search_name = input('请输入要查询的学生的姓名：')
    global info  # 声明全局变量
    for i in info:
        if search_name == i['name'] :
            print('查询到的学生信息如下--------------------------')
            print(f"学生的学号：{i['id']} , 姓名：{i['name']},   手机号：{i['tel']}")
            break
    else:
        print('查无此人.....')


# 显示所有学生信息
def print_all():
    '''显示所有学生信息'''
    print('学号\t姓名\t手机号')
    # 打印所有学生的数据
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")




while True:
# 1. 显示功能界面
    info_print()

# 2. 用户输入功能序号
    user_num = int(input('请输入功能序号：'))

# 3. 按照用户输入的功能序号，执行不同的功能（函数）

    if user_num == 1:
        # print('添加')
        add_info()
    elif user_num == 2:
        # print('删除')
        del_info()
    elif user_num == 3:
        # print('修改')
        modify_info()
    elif user_num == 4:
        # print('查询')
        search_info()
    elif user_num == 5:
        # print('显示所有')
        print_all()
    elif user_num == 6:
        # 退出系统
        exit_flag = input('确定要退出吗？yes or no：')
        if exit_flag == 'yes':
            break   # break是最主要的
    else:
        print('输入的功能序号有误')

# 这个退出系统功能，不用函数去做，1.代码比较简单 2.有一个必要的功能，封装到函数里面可能会出问题
# 退出系统依赖于break，break是当一定条件成立，终止循环用的。终止的是就近的这一层循环，如果把这些代码封装
# 一个函数里面去，这个时候跟while True循环不在一起了，就有可能发生问题的。
