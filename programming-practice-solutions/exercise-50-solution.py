# server has port open and client will communicate through that port

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server = 'pythonprogramming.net'

def port_scan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,26):
    if port_scan(x):
        print ('Port',x,'is open++++')
    else:
        print ('Port',x,'is closed')
