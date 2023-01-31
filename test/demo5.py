def test(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))

b = 100
test(b)    # 这是不可变类型数据

c = [11, 22]
test(c)    # 这是可变类型数据