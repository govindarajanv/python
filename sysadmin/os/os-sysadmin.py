import os

#name of the operating system
print ("Name of OS:", os.name)

#current working directory
print ("Current working directory:",os.getcwd())

#printing CPU count
print ("Total CPU Count:", os.cpu_count())

#getting name of a environment variable
print ("JAVA HOME Env value is ",os.getenv('JAVA_HOME'))

#printing name of the logged in user
print ("Logged in user is ", os.getlogin())

#listing the current directory
print ("Contents of current directory:", os.listdir(path=None))

#creating the directory
print ("Creating a directory..")
os.mkdir('govind')

#executing an OS command
print ("Output of the OS command:[")
os.system('ls -lrt')
print ("]")

#printing name of the login user
print ("Deleting the directory..")
os.rmdir('govind')

