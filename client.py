from socket import *

host = gethostname()
port = 1234
ADDR = (host,port)
BUFSIZ = 1024

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
print('conneting...')
while True:
    data = input('>>>>')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode())
tcpCliSock.close()
