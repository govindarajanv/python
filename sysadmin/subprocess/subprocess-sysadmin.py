import subprocess
print ("listing of file using ls -l:")
retcode = subprocess.call(["ls", "-l"])
print ("checking..listing of file using ls -l:")
subprocess.check_call(["ls", "-l"])

