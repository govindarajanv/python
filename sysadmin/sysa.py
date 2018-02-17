import os
import time
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

