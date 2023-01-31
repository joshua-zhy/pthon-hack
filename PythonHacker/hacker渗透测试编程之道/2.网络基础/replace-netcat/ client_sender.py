import socket

def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接到目标主机
        client.connect((target, port))

        if len(buffer):
            client.send(buffer)

        while True:# 现在等待数据回传
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break

            print  (response)

            # 等待更多的输入
            #buffer = raw_input("")
            buffer = input("")
            buffer += "\n"

            # 发送出去
            client.send(buffer)

    except:
        print ("[*] Exception! Exiting.")

    #关闭连接
    client.close()
