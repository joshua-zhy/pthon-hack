mystr = 'hello world and itcast and itsmail and Python'

# 1. find()
print(mystr.find('and')) # 输出的是12，以为下标是从0开始数的
print(mystr.find('and',15,30))#range 指定的范围 23
print(mystr.find('ands')) # -1,ands字串不存在

# # 2. index
print(mystr.find('and')) # 12
print(mystr.find('and',15,30)) #23
# print(mystr.index('ands')) #如果index查找字串不存在，报错

# 3. count()
print(mystr.count('and')) #3
print(mystr.count('and',15,30)) #1
print(mystr.count('ands')) #0

# 4. rfind()
print(mystr.rfind('and')) #35
print(mystr.find('ands')) #-1 #如果没找到，则返回-1

# 5. rindex()
print(mystr.rindex('and')) #35  #就算是到着找，它的下标还是从左到右从下标0开始的
print(mystr.rindex('ands'))#没找到报错


# 遇到列表、字典，内部的数据可以直接修改，修改的就是原列表或者原字典。叫做可变类型。
# 字符串是一个不可变类型的数据

mystr = 'hello world and itcast and itheima and Python'
# replace() 把and换成he replace函数有返回值，返回值是修改后的字符串
new_str = mystr.replace('and','he')
# new_str = mystr.replace('and','he',1)
# 替换次数如果超出字串出席那的次数，表示替换所有这个字串
# new_str = mystr.replace('and','he',10)
print(mystr)
print(new_str)

# 调用了replace函数后，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
# 说明字符串是不可变数据类型
# 数据是否可以改变划分为 可变类型，不可变类型

# 2. split()  分割，返回一个列表，丢失分割字符
list1 = mystr.split('and')
print(list1)

# 3. join() 合并列表里面的字符串数据为一个大字符串
mylist = ['aa','bb','cc']
new_str = '...'.join(mylist)
print(new_str)


