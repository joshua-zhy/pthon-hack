passward = input('请输入您的密码：')
print(f'您输入的密码是：{passward}')

# input接收到的数据类型都是字符串
print(type(passward))


num = input("请输入一个数字：")
print(num)
print(type(num))

# 强制转换为int类型
print(type(int(num)))
print(type(int(num)))


'''
因为得到数据类型并不是程序想要的数据类型，这个时候需要借助数据类型转换的函数来转换
'''
num = 1
str1 = '10'

# 1.将数据转换成浮点类型 float()
print(type(float(num)))
print(float(num))
print(float(str1))

# 2. 将数据转换成字符串型 str()
print(type(str(num)))

# 3. 序列转换成元组 tuple()
list1 = [10,20]
print(type(list1))
print(type(tuple(list1)))
print(tuple(list1))  	 # (100, 200)

# 4. 将一个元组转换成序列 list()
t1 = (100,200)
print(list(t1)) 		# [100, 200]

# 5. eval() 计算在字符串中的有效Python表达式，并返回一个表达式。把字符串中的数据转换成他原本的类型
str3 = '1'
str4 = '2.1'
str5 = '(10,20)'
str6 = '[10,20]'
print(type(eval(str3)))   # <class 'int'>
print(type(eval(str3) + 8 ))   # <class 'int'>

print(eval(str3)+3)