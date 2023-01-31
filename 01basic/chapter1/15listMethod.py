name_list = ['TOM','Lily','Rose']

# 1.index()
print(name_list.index('TOM'))  #返回 0
# print(name_list.index('TOMs'))  没有找到，报错

# 2. count()
print(name_list.count('TOM'))#!
# print(name_list.count('TOMS')) # 报错

# 3.len()
print(len(name_list)) # 输出3


# 1. 列表数据是可变的  -- 列表是可变类型
# 2. append函数追加数据的时候如果是一个序列，追加整个序列到列表的结尾

name_list = ['TOM','Lily','ROSE']
name_list.append('xiaoming')
name_list.append([11,22])
name_list.append(11)
print(name_list)  # 输出结果为：['TOM', 'Lily', 'ROSE', 'xiaoming', [11, 22], 11]

# extent() 追加数据是一个序列，把数据序列里面的数据拆开然后逐一追加到列表的结尾
name_list = ['TOM','Lily','ROSE']
name_list.extend('xiaoming')
# 把序列拆开，逐一的放到列表中
name_list.extend(['xiaoming','xiaojun'])
print(name_list) 
 # 输出结果为：['TOM', 'Lily', 'ROSE', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g', 'xiaoming', 'xiaojun']

name_list = ['Tom','Lily','ROSE']

# remove
# 1. del
# del name_list
# print(name_list) 已经把列表已经删除，已经没有列表了

# del 也可以指定下标的数据
# del name_list[0]
# print(name_list)   # 输出的结果 ['Lily', 'ROSE']


# 2. pop() 删除指定下标的数据，如果不指定下标，默认删除最后一个数据
# 无论是按照下标还是删除最后一个，pop函数都会返回这个被删除的数据. 比较厉害的是删除一个数据能用一个变量去接收
del_name = name_list.pop()
del_name = name_list.pop(1)
print(del_name)
print(name_list)

# 3. remove(数据) 按照指定的数据进行删除的
# name_list.remove('ROSE')
# print(name_list)

# 4. clear() -- 清空
# name_list.clear()
# print(name_list)  # 直接清空整个数据

name_list = ['TOM','Lily','ROSE']

# 修改指定下标的数据
# name_list[0] = 'aaa'
# print(name_list) # ['aaa', 'Lily', 'ROSE']

# 2. 逆序 reverse()
list1 = [1, 3, 4, 2, 5]
# list1.reverse()
# print(list1)

# 3. sort() 排序：升序（默认）和 降序
# list1.sort()  # 升序
list1.sort(reverse=False)  # 升序 [1, 2, 3, 4, 5]
list1.sort(reverse=True)   # 降序 [5, 4, 3, 2, 1]
print(list1)

# （5）赋值
name_list = ['tom','lucy','jack']
list1 = name_list.copy()
print(list1)
print(name_list)


name_list = ['tom','rose','jack']
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1
    
    
# for循环的代码量要少于while的代码量
# 一般在工作岗位下，涉及到遍历序列当中的数据的话，一般优选于for循环
name_list = ['tom','rose','jack']
for i in name_list:
    # 遍历序列中的数据
    print(i)
    


name_list = [['TOM', 'Lily','Rose'], ['张三','李四','王二'], [ '小红', '小绿', '小蓝']]
# print(name_list)
# 列表嵌套的时候的数据查询
print(name_list[0])
print(name_list[0][0])





