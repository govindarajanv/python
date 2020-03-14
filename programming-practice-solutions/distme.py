import threading
from queue import Queue
import time

# 10 threads and 20 jobs

print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(0.5)

    # after printing lock is released
    with print_lock:
        print (threading.current_thread().name, worker)

# does actual threading operation
def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()


q = Queue()

for x in range(10):
    t = threading.Thread(target=threader)

    # to make it work in the background
    t.daemon = True
    t.start()

#note the start time
start = time.time()

for worker in range(20):
    q.put(worker)

# block until all tasks are done
q.join()

print ('Entire job took:', time.time()-start)
