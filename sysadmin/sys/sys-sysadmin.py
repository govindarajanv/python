import sys

#Get windows version
print ("Windows OS Version:",sys.getwindowsversion())

#Get value of PATH environment variable
print ("Env variable PATH:",sys.path)

#Get platform name
print ("platform is:",sys.platform)

#Command line arguments
print ("File name from command line argument:",sys.argv[0])
