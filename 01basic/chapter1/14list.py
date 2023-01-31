name_list = ['TOM','Lily','ROSE']
print(name_list)   # ['TOM', 'Lily', 'ROSE']
# 根据下标进行输出
print(name_list[0])  # 输出 TOM
print(name_list[1])  # 输出 Lily
print(name_list[2])  # 输出 ROSE


name_list = ['TOM','Lily','ROSE']
# 1. in  如果在里面就返回true，否则false
print('TOM' in name_list)
print('TOMS' in name_list)

# 2. not in   这个跟in相反
print('TOM' not in name_list)
print('TOMS' not in name_list)



name_list = ['TOM','List','ROSE']

# 需求：注册邮箱，用户输入一个账户名，判断这个账号是否存在，如果存在，提示用户，否则提示可以注册
name = input("请输入您的邮箱账号名：")
if name in name_list:
    # 提示用户名已经存在
    print(f'您输入的名字是{name}，此用户已经存在')
else:
    # 提示可以注册
    print(f'您输入的名字是{name},可以注册')

