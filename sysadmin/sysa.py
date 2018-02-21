import os
import time
import paramiko

class Query(object):
    def __init__(self, objective, environment):
        self.objective = objective
        self.environment = environment
    def set_objective(self, objective):
        self.objective = objective
    def set_environment(self, environment):
        self.environment = environment

    def action(self):
        print ("actionizing %s from %s " % (self.objective, self.environment))
	# Create the SSH client.
        ssh = paramiko.SSHClient()
	command = "df"
	host = "10.1.1.30"
	port = 22
	username = "vagrant"
	key = "/root/.ssh/id_rsa"
	private_key = paramiko.RSAKey.from_private_key_file (key)
	password = "vagrant"
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(host, port, username, password, private_key)
	# Send the command (non-blocking)
        stdin, stdout, stderr = ssh.exec_command(command)

        # Wait for the command to terminate
        while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
            time.sleep(1)

        stdoutstring = stdout.readlines()
        stderrstring = stderr.readlines()
	for line in stdoutstring:
          #print (line)
	  sub_str = line.split(" ")
          print ("%s%s" % (sub_str[len(sub_str)-1].strip().ljust(30) , sub_str[len(sub_str)-2].strip().ljust(30)))
          #print (sub_str)
		

def getEnvDetails():
	choice=True
        while choice:
            os.system("clear")
            print("""
            1. App IQA
            2. App UAT
            3. Exit/Quit
	    """)
	    time
	    choice=raw_input("Please choose your environment:")
	    if choice=="1":
		environment="vt_iqa"
		choice = None
	    elif choice=="2":
		environment="vt_uat"
		choice = None
	    elif choice=="3":
		 choice = None
	    else:
	       print("\n Not Valid Choice Try again")
	print ("Chosen env is" )
	print (environment)
	time.sleep(1)
	return environment

if __name__ == '__main__':
	choice=True
	while choice:
	    os.system("clear")
	    print("""
	    1.Get the list of installed packages
	    2.Get the status of services running with port
	    3.Get the free space
	    4.Exit/Quit
	    """)
	    choice=raw_input("What would you like to do? ")
	    if choice=="1":
	      objective = "list_packages"
	      environment = getEnvDetails()
	      print("\nPackages installed are:")
	    elif choice=="2":
	      print("\n Services that are being run are:")
	    elif choice=="3":
	      print("\n Free Disk Space available are:")
	    elif choice=="4":
	      print("\n Goodbye") 
	      choice = None
	    else:
	       print("\n Not Valid Choice Try again")
	time.sleep(1)
	query = Query(objective,environment )
	os.system("clear")
	query.action()
	# Get current working dir
	print (os.getcwd())

