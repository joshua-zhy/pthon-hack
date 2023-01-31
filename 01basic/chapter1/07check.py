if True:
    print('条件成立了')
# 下面的代码没有缩进到if语句块，所以和if条件无关
print('这个代码执行吗？')


age = 20
if age >= 18:
    print('已经成年可以上网')

# 注意：不缩进的语句，跟if语句没有关系了。
print('系统关闭')


# 注意：input接受用户输入的数据是字符串类型，这时需要转换为int类型才能进行判断
age =int( input('请输入您的年龄：'))
if age >= 18:
    print(f'您输入的年龄是{age},已经成年可以上网')
    

age =int( input('请输入您的年龄：'))
if age >= 18:
    print(f'您输入的年龄是{age},已经成年可以上网')
else:
    print(f'你输入的年龄是{age}，小朋友，回家写作业去')


age = int(input('请输入您的年龄'))
if age < 18:
    print(f'您输入的年龄是{age}，童工')
elif (age >= 18) and (age <= 60):
    print(f'您输入的年龄是{age}，合法')
elif age > 60:
    print(f'您输入的年龄是{age}，退休')


age = int(input('请输入您的年龄'))
if age < 18:
    print(f'您输入的年龄是{age}，童工')
#  条件的简化写法
elif 18 <= age <= 60:
    print(f'您输入的年龄是{age}，合法')
elif age > 60:
    print(f'您输入的年龄是{age}，退休')

