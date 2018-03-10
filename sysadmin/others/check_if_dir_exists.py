#python script to check if a directory exists or not
import os

if os.path.isdir("/home/vagrant/workspace/python/sysadmin"):
    print ("Yes, Directory exists")
else:
    print ("No, Directory does not exist")
