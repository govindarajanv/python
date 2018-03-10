#System monitoring
import subprocess

#Get OS details
print ("Getting OS Details")
uname = "uname"
uname_args = "-a"
subprocess.call([uname, uname_args])

# Get Disk space
print ("Getting Disk Space")
disk_space = "df"
disk_space_args = "-hk"
subprocess.call([disk_space, disk_space_args])

# Get Disk usage
print ("Getting Disk Usage")
subprocess.call("du -hs", shell=True)
