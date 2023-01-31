# 猜拳游戏
import random

player = int(input('请出拳：0--石头；1--剪刀；2--布'))
# computer = 1
computer = random.randint(0,2)
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜，哈哈哈 ')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')


# 随机数的使用

'''
步骤：
    1.导入模块
    import random
    2.使用这个模块中的功能
    random.randint
'''
# import random
# num = random.randint(0,2)
# print(num)


# 三目运算符
a = 1
b = 2
c = a if a > b else b
print(c)

aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa
print(cc)

    
