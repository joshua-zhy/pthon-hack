print('hello world')
print('hello\nworld')  # hello world直接换行输出
print('\thello')    # 前面输出空格再输出hello


# 在python中，print()默认自带end='\n'这个换行结束符，用户可以按照需求更改结束符

print('hello', end='\n')
print('world')

print('hello', end='\t')
print('hello')

print('hello', end='...')
print('world')


print("hello",end="\n")
print("world")