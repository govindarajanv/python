#System monitoring
import subprocess

#Get OS details
def get_os_info():
  print ("\n\n")
  print ("Getting OS Details")
  print ("\n")
  uname = "uname"
  uname_args = "-a"
  subprocess.call([uname, uname_args])
  print ("\n\n")

# Get Disk space
def check_space():
  print ("Getting Disk Space")
  print ("\n")
  disk_space = "df"
  disk_space_args = "-hk"
  subprocess.call([disk_space, disk_space_args])
  print ("\n\n")

# Get Disk usage
def check_disk_usage():
  print ("Getting Disk Usage")
  print ("\n")
  subprocess.call("du -hs", shell=True)
  print ("\n\n")

def main():
  get_os_info()
  check_space()
  check_disk_usage()

main()
