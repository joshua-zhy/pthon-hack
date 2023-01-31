import socket 

def udp_client(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (ip, port)
    
    while True:
        data = input("Please input your name: ")
        if not data:
            continue
        s.sendto(data.encode(), addr)
        response, addr = s.recvfrom(1024)
        print(response.decode())
        if data == "exit":
            print("Session is over from the server %s:%s\n" % addr)
            break
    
    s.close()

if __name__ == '__main__':
    server_ip = "127.0.0.1"
    server_Port = 8888
    udp_client(server_ip,server_Port)
    