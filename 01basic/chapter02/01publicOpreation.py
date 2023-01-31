# 运算符：+（合并的作用）

str1 = 'aa'
str2 = 'bb'

list1 = [1,2]
list2 = [10,20]

t1 = (1,2)
t2 = (10,20)

dict1 = {'name':'tom'}
dict2 = {'age':30}

# 1. + : 合并
print(str1+str2)      # 输出 aabb
print(list1+list2)    # 输出 [1, 2, 10, 20]
print(t1+t2)          # 输出 (1, 2, 10, 20)
print(dict1+dict2)    # 报错：字典不支持合并运算


 
# 运算符：*（复制的作用）

str1 = 'a'
list = ['hello']
t1 = ('world',)

#   *:复制   支持字符串、列表、元组
print(str1 * 5)  # 输出aaaaa
print('-' * 10)  # 输出10个----------
print(list * 5)  # 输出['hello', 'hello', 'hello', 'hello', 'hello']
print(t1 * 5)    # 输出 ('world', 'world', 'world', 'world', 'world'

# 
# 运算符：in、not in（判断元素是否存在）

str1 = 'abcd'
list1 = [10,20,30]
t1 = (100,200,300)
dict1 = {'name':'Python', 'age':30}
# in 和 not in

# 1. 字符a是否存在
print('a' in str1)  # 输出 True
print('a' not in str1)  # 输出 false

# 2. 数据10是否存在
print(10 in list1)   # 输出True
print(10 not in list1)  # 输出False

# 3. 100是否存在
print(100 in t1)    # 输出 True
print(100 not in t1)   # 输出Fasle

# 4. name是否存在
print(dict1)
print('name' in dict1)   # True
print('name' not in dict1)  # False
print('name' in dict1.keys()) # True
print('name' in dict1.values() ) # False


