
# 字符串的使用区别

a = 'hello' \
    ' world'
print(a)   # 输出一行 hello world

c = '''hello 
world'''
print(type(c))
print(c)       # 换行输出hello world


d = """hello 
world"""
print(type(d))  # <class 'str'>
print(d)        # 会直接换行输出

# 打印 I'm Tom，使用单引号，必须使用转移字符，把他转义过去
e = 'I\'m Tom'
print(e)

# 要是有单引号出现可以使用双引号括住
f = "I' love Tom"
print(f)


# 字符串的输出 

name = 'Tom'
print('我的名字是%s' % name)
print(f'我的名字是{name}')
1

# 字符串的输入
password = input('请输入您的密码')
print(f'您输入的密码是{password}')
# input接收到的用户输入的数据都是字符串
print(type(password))

