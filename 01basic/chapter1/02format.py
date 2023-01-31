age = 18
name = 'TOM'
weight = 75.5
stu_id = 1

print('今年我的年龄是%d' % age)
print('我的名字叫%s' % name)
print('我的体重是%.3f' % weight)
print('我的体重是%03d' % stu_id)  # 不够三位，用0补全

print('我的名字叫：%s ，我的年龄是：%d' % (name,age))
print("我的名字叫：%s，我的年龄是：%d" % (name,age+1))  # 年龄加一岁

print("我的名字叫：%s，今年的年龄是：%d，我的体重是：%s，我的学号是：%03d" % (name,age,weight,stu_id))


name = "TOM"
age = 18
weight = 75.5

# %s比较强大
print('我的名字叫：%s，我的年龄是：%s，我的体重是：%s' % (name,age,weight))


name = 'TOM'
age = 16

# 语法：f'{表达式}'
# 这样的输出格式更加高效和简洁

print(f'我的名字叫{name},我的年龄为{age}')

