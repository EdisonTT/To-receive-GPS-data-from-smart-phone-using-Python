import socket as soc
s = soc.socket()
host = '192.168.43.70'
port = 12345
s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)
c,addr = s.accept()
while True:
    print(c.recv(2048).decode('ascii'))
