sum = 0
i = 1
while i <= 100:
     sum +=i
     i+=1
print(sum)

j = 0
while j < 5:
    # 一行星星的打印
    i = 0
    while i <= j:
        # i表示每行里面星星的个数，这个数字要和行号相等所以i要和j联动
        print('*', end='')
        i += 1
    # 利用空的print来进行换行
    print()
    j += 1