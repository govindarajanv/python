import psutil
###########################
#       CPU             
###########################
#Get CPU times
print("CPU time:",psutil.cpu_times())

#Get CPU Count
print ("CPU count:", psutil.cpu_count())

#CPU Percentage
print ("CPU Usage:",psutil.cpu_percent())

#CPU Stats
print ("CPU Stats:",psutil.cpu_stats())

#CPU Freq
print ("CPU Freq:",psutil.cpu_freq())

############################
#   Memory
############################
#Get Virtual Memory
print ("Virtual Memory:", psutil.virtual_memory())

#Get Swap Memory
print ("Swap Memory:", psutil.swap_memory())

############################
#   Disk
############################
#get disk partitions
print ("Disk partitions:",psutil.disk_partitions())

#get disk uage
print ("Disk Usage:",psutil.disk_usage('/'))

#get disk IO
print ("Disk Usage:",psutil.disk_io_counters(perdisk=False))

##############################
#   OTHERS
#############################
#get users
print ("Users:",psutil.users())

#Get boot time
print ("Boot time:", psutil.boot_time())

#Get Pids
print ("Pids:",psutil.pids())
p = psutil.Process(7152)
print ("Process details for pid:",p)
print ("Exe:",p.exe())
print ("CWD:",p.cwd())
print ("cmdline:",p.cmdline())
print ("Parent Process:",p.parent())
print ("Parent Process id:",p.ppid())
print ("creation time of the  Process:",p.create_time())
# there are other features like suspend, terminate ,resume of processes and querying process's memory utilization


