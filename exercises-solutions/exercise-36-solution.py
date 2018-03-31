import subprocess

#Execute OS commands

#formatted
#subprocess.call("dir",shell=True)

#unformatted
output = subprocess.check_output("dir",shell=True)
#print(output)

print("============================================================")
#subprocess.Popen("dir", shell = False)
print("============================================================")
subprocess.Popen("dir", shell = True)
print("============================================================")
