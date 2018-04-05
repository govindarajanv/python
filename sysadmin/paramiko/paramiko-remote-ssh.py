import paramiko
from scp import SCPClient

k = paramiko.RSAKey.from_private_key_file("C:/Users/vishnuch/.ssh/id_rsa")
c = paramiko.SSHClient()

c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print ("About to connect...\n\n")

c.connect( hostname = "216.178.190.104", username = "govindarajan.vishnuchithan", pkey = k )
print ("connected")
commands = [ "df -hk", "du -hs" ]
for command in commands:
	print ("Executing {}".format( command ))
	stdin , stdout, stderr = c.exec_command(command)
	print (stdout.read())
	print( "Errors")
	print (stderr.read())

#scp operations
scp = SCPClient(c.get_transport())
# fetch from server
scp.get('data.list')
# push to server
scp.get('D:\\code\\python\\sysadmin\\paramiko\\node.list')

c.close()
