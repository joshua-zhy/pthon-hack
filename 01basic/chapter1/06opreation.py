a = 10
a += 1
print(a)  # 11

b = 10
b *= 3
print(b)  # 30

# 注意：先算复合赋值运算符右侧的表达式，算复合赋值运算
c = 10
c += 1 + 2
print(c)  # 13
# c++  py 没有 ++
# 测试
d = 10
d *= 1 + 2
print(d)  	# 30 说明先算复合赋值运算符右侧的表达式，再算复合赋值运算


# 逻辑运算符的运用

a = 0
b = 1
c = 2

# 1.and
print((a < b) and (a < c))   # True
print(a > b and a < c)		# False

# 2.or
print(b > c or a < c)  # True

# 3.not
print(not a < b)	# False

# 程序员的习惯
# 加小括号为了避免歧义，增加优先级
