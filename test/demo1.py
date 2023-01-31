
mystr = 'hello world and itcast and itheima and Python'

# 2. split()  分割，返回一个列表，丢失分割字符
list1 = mystr.split('and')
print(list1)

# 3. join() 合并列表里面的字符串数据为一个大字符串
mylist = ['aa','bb','cc']
new_str = '...'.join(mylist)
print(new_str)

new_str = '@'.join(mylist)#原来的字符没有变
print(new_str)

# ['hello world ', ' itcast ', ' itheima ', ' Python']
# aa...bb...cc
# aa@bb@cc

# 一、字符串对齐
# mystr.ljust(10) 左对齐
# mystr.rjust(10) 右对齐
# mystr.rjust(10,'.') 以点作为填充效果
# mystr.center(10) 中间居中
# mystr.center(10,'.') 以点填充空白的地方



# 二、大小写转换
mystr = 'hello world and itcast and itheima and Python'
# 1. capitalize() 字符串首字母大写
# new_str = mystr.capitalize()
# print(new_str)

# 2. title():字符串中每个单词首字母大写
# new_str = mystr.title()
# print(new_str)

# 3. upper():小写转大写
# new_str = mystr.upper()
# print(new_str)

# 4. lower()：大写转小写
# new_str = mystr.lower()
# print(new_str)


# 三、删除空白字符
str1 = "      hello world and itcast and itheima and Python  "
# 1. lstrip():删除字符串左侧空白字符
# print(str1)
# new_str = str1.lstrip()
# print(new_str)

# 2. rstrip():删除字符串右侧空白字符
new_str = str1.rstrip()
print(str1)
print(new_str)

# 3. strip():删除字符串两侧空白字符
# new_str = str1.strip()
# print(new_str)

# 判断开头或结尾
mystr = 'hello world and itcast and itheima and Python'
# 1. startswith(字串，开始位置下标，结束位置下标):判断字符串是否以某个字串开头
print(mystr.startswith('hello'))
print(mystr.startswith('hel'))
print(mystr.startswith('hels'))
print(mystr.startswith('hell',0,10))# 开始位置下标和结束位置下标可以省略

# 2. endswich(字串，开始位置下标，结束位置下标)，始位置下标和结束位置下标可以省略
print(mystr.endswith('Python'))
print(mystr.endswith('Pythons'))

# 判断
# 3. isalpha():字母  纯字母才可以，如果中间有空格返回的false
print(mystr.isalpha())

# 4. isdigit():数字，中间也不能有空格，否则返回false
print(mystr.isdigit())
mystr1 = "12345"
print(mystr1.isdigit())

# 5. isalnum():数字或字母或组合
print(mystr1.isalnum()) # True
print(mystr.isalnum())  # False 因为中间有空格
mystr2 = 'abc123'
print(mystr2.isalnum())

# 6. isspace():判断是否是空白，是返回True
print(mystr.isspace())  # False
mystr3 = ' '
print(mystr3.isspace())	 # True
