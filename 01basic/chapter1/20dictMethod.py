'''
新增数据的写法：字典序列[key] = 值
 这里的字典为可变类型，打印原字典名，就能看到修改新增之后的数据。之前的元组是不可变类型，是不能修改内部数据的。
注意: 如果key存在则修改这个key对应的值；如果key不存在则新增此键值对
'''

dict1 = {'name': 'TOM' , 'age':20 , 'gender': '男' }

# name这个键存在这个字典中，所以修改键值对
dict1['name'] = 'ROSE'
print(dict1)  # 输出修改后的字典 {'name': 'ROSE', 'age': 20, 'gender': '男'}

# id这个key不存在这个字典中，所以新增此键值对
dict1['id'] = 110
print(dict1)   # 输出新增后的字典{'name': 'TOM', 'age': 20, 'gender': '男', 'id': 110}

dict1 = {'name': 'TOM', 'age': 20 , 'gender': '男'}


# 1.del 删除字典或指定的键值对

# 删除字典
# del(dict1)
# print(dict1)   # 报错，说明已经删除了

# 删除指定的字符串
# del dict1['name']  # 删除key为name的键值对
# del dict1['names']  # 如果删除的内容不存在就会报错
# print(dict1)		# {'age': 20, 'gender': '男'}

# 2. clear() 清空字典
dict1.clear()
print(dict1)      # 输出{}


    
dict1 = {'name':'tom', 'age':20 , 'gender':'男'}

# dict1['name'] = 'lily'
# print(dict1)     # {'name': 'lily', 'age': 20, 'gender': '男'}

dict1['id'] = 2020
print(dict1)    # {'name': 'tom', 'age': 20, 'gender': '男', 'id': 2020}

# 查找数据



# 可迭代的对象指代的是可以用for遍历的对象

dict1 = {'name':'tom', 'age': 20 , 'gender':'男'}

# 1. [key]
# print(dict1['name'])    #  输出tom 
# print(dict1['names'])   # 如果查找的值是不存在的key，则会报错

# 2.函数

# 2.1 get()
# 语法： 字典序列.get(key,默认值)

# print(dict1.get('name'))   # tom
# print(dict1.get('names'))  # 如果键值不存在，返回None
# print(dict1.get('names','不存在')) # 如果键值不存在，返回“不存在”

# 2.2 keys() 查找字典中所有的key，返回可迭代对象
print(dict1.keys())  # 输出 dict_keys(['name', 'age', 'gender'])

# 2.3 value() 查找字典中所有的value，返回可迭代对象
print(dict1.values())  # 输出 dict_values(['tom', 20, '男'])

# 2.4 items() 查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是字典的key，元组数据2是字典key对应的值
print(dict1.items())  # 输出dict_items([('name', 'tom'), ('age', 20), ('gender', '男')])




# 6.3 字典的遍历

# key遍历

dict1 = {'name':'tom', 'age':20 , 'gender': '男'}

for key in dict1.keys():
    print(key)
'''
输出结果：
       name
       age
       gender
'''    


# value遍历

dict1 = {'name':'tom', 'age':20, 'gender':'男'}

for value in dict1.values():
    print(value)
    
'''
输出结果：
		tom
		20
		男
'''

# 键值对遍历
# dict1.items 可迭代对象的内部是元组
dict1 = {'name':'tom', 'age': 20 , 'gender': '男'}
for item in dict1.items():
    print(item)
'''
输出结果：
        ('name', 'tom')
        ('age', 20)
        ('gender', '男')
'''


# 键值对拆包遍历

dict1 = {'name':'tom', 'age':'20', 'gender':'男'}

# xx.items():返回可迭代对象，内部是元组，元组有2个数据
# 元组数据1是字典的key，元组数据2是字典的value

for key,value in dict1.items():
    # print(key)
    # print(value)
    print(f'{key}={value}')

'''
输出的内容是：

    	name=tom
   		age=20
    	gender=男
'''



# 6.4 字典小总结

 

# 定义字典
# dict1 = {'name':'TOM', 'age':30}
# dict2 = {}
# dict3 = dict()

# 常见操作
#     增/改
# 字典序列[key] = 值

# 查找
#     字典序列[key]
#     keys()
#     values()
#     items()




