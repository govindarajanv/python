# server has port open and client will communicate through that port

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print (s)

server = 'pythonprogramming.net'
port = 80
#To get server ip
server_ip = socket.gethostbyname(server)
print (server_ip)

request = "GET / HTTP/1.1\nHOST: "+server+"\n\n"
print  ("request:", request)

s.connect((server,port))
s.send(request.encode())

# number in the bracket is the buffer size
result = s.recv(4096)

while (len(result) > 0):
    print (result)
    result = s.recv(1024)
