import subprocess
subprocess.call('df -hk',shell=True)
# command without suppress
subprocess.call("ping -c 10.1.1.1",shell=True)
# command with suppress
subprocess.call("ping -c 10.1.1.1",shell=True,stdout=open('output.txt','w'),stderr=subprocess.STDOUT)
# Get return status
print ("Sub process call with check on return status")
result=subprocess.call("ls testfile",shell=True)
if result == 0:
    print ("file exists")
else:
    print ("file does not exist")

import platform
print (platform.system())
print (platform.release())

p = subprocess.Popen("wc -c", shell=True, stdin=subprocess.PIPE)
# This needs to be fixed
#print (p.communicate("charactersinword"))
