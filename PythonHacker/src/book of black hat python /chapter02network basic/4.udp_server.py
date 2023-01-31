import socket
 
 
def udp_server(ip,port): 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip,port))
    print(f"UDP bound on port {port}...")
    
    while True:
        data, addr = s.recvfrom(1024)
        print("Receive from %s:%s" % addr)
        if data == b"exit":
            s.sendto(b"Good bye!\n", addr)
            continue
        s.sendto(b"Hello %s!\n" % data, addr)
    
    
    
if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 8888
    udp_server(ip,port)
    
    