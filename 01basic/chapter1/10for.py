
str1 = 'ilovepython'
for i in str1:
    # 当某些条件成立，退出循环  条件：i取到字符e的时候退出循环
    if i == 'e':
        # continue
        break
    print(i)
   

# 所谓else指的是循环正常结束之后要执行的代码，
# str1 = 'ilovepython'
# for i in str1:
#     print(i)
# else:
#     print('循环正常结束执行的else代码')