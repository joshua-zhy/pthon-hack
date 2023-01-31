 
# 打印横线图形


def print_line():
    print('-' * 20)

# 函数嵌套调用，实现多条横线
def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1

print_lines(5)

 
# 任意三个数求平均值

#  任意三个数求平均值
# Python语言当中，做除法运算，不管参与运算的是不是浮点数，只要是除法，结果就是浮点数。

def sum_num(a,b,c):
    return a + b + c
    
def average_num(a, b ,c):
    # 先求和，再除以3
    sumResult = sum_num(a, b, c)
    return sumResult / 3

averageResult = average_num(1, 2, 3)
print(averageResult)   # 输出结果为 2.0
