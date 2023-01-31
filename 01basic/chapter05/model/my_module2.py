# 有all列表控制着导入行为，导致只导入all列表里面的功能。

# 1. 定义多个功能，把某个功能添加到__all__
__all__ = ['testA']

def testA():
    print('testA')

def testB():
    print('testB')

