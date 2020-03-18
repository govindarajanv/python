# server has port open and client will communicate through that port

import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = 'Pythonprogramming.net'


def port_scan(port):

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print ('Port',x,'is open++++')
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()

q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,10000):
    q.put(worker)


q.join()
