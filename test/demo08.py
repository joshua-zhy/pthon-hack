import subprocess

# res = subprocess.call('ls -l',shell=True)

# 多个命令参数通过列表的形式提供时不需要提供shell=True参数：
res = subprocess.call(['ls','-l'])


# check_output
# subprocess.check_output(args, *, stdin = None, stderr = None, shell = False, universal_newlines = False)
# 在子进程执行命令，以字符串形式返回执行结果的输出。
# 如果子进程退出码不是0，抛出subprocess.CalledProcessError异常，异常的output字段包含错误输出：


print(res)
