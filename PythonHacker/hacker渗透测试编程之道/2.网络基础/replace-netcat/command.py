import sys
import getopt

# 定义一些全局变量
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def usage():
    print("BHP Net Tool" )
    print("\n")
    print ("Usage: replacenetcat.py -t target_host - p port")#使用方法
    print ("-l --listen              - listen on [host]:[port] for incoming connections")
    print ("-e --execute=file_to_run -execute the given file upon receiving a connection")
    print ("-c --command             - initialize a commandshell")
    print ("-u --upload=destination  - upon receiving connection upload a file and write to [destination]")
    print("\n")
    print("\n")
    print ("Examples:")
    print ("replacenetcat.py -t 192.168.0.1 -p 5555 -l -c")
    print ("replacenetcat.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print ("replacenetcat.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print ("echo 'ABCDEFGHI' | python ./bhpnet.py -t 192.168.11.12 -p 135")
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not  len(sys.argv[1:]):
        usage()

    try:# 读取命令行选项,若没有该选项则显示用法
        # getopt.getopt(args, shortopts, longopts=[])
        # args指的是当前脚本接收的参数，它是一个列表，可以通过sys.argv获得 sys.args[1:] 获取想· 
        # shortopts 是短参数　　啥是短参数啊？　　类似于　这样：python test.py -h # 输出帮助信息
        # longopts 是长参数　　啥是长参数啊？　　类似于　这样：python test.py -help # 输出帮助信息
        # getopt.getopt(args, shortopts, longopts=[])
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print (str(err))
        usage()


    for o,a in opts:#进入相对应的功能模块
        if o in ("-h","--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False,"Unhandled Option"

    if not listen and len(target) and port > 0:#我们是进行监听还是仅从标准输入读取数据并发送数据？

        # 从命令行读取内存数据
        # 这里将阻塞,所以不再向标准输入发送数据时发送CTRL-D
        buffer = sys.stdin.read()
        client_sender(buffer)# 发送数据

    # 我们开始监听并准备上传文件,执行命令
    # 放置一个反弹shell
    # 取决于上面的命令行选项
    if listen:
        server_loop()