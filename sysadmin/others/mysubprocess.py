import subprocess

#
print (subprocess.call(['du', '-hs']))
print (subprocess.call('du -hs $HOME', shell=True))

#result = subprocess.Popen(['uname', '-sv'], stdout=subprocess.PIPE)
#uname = res.stdout.read().strip()
#print (uname)
