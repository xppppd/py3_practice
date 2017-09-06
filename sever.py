from socket import *
from time import *

tcpSerSock = socket(AF_INET,SOCK_STREAM)

host = gethostname()
port = 1234
BUFSIZ = 1024
ADDR = (host, port)

tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waitting for connetion...')
    cs, addr = tcpSerSock.accept()
    print('...Got connect from', addr)
    while True:
        data = cs.recv(BUFSIZ)
        if not data:
            break
        print(data.decode())
        data = input('>>>>')
        if not data:
            break
        cs.send(data.encode())
    cs.close()