from fabric.api import run,env
from fabric.api import local

# print hello world
def hello():
    print ("Hello World")

# execute commands locally
def list():
    local('dir')

# maintain list of hosts and run commands on all those nodes
# fab -P uptime # tells Fabric to run the commands asynchronously (in parallel)

env.hosts = [ 'govindarajanv1.mylabserver.com','govindarajanv2.mylabserver.com','govindarajanv3.mylabserver.com','govindarajanv4.mylabserver.com','govindarajanv5.mylabserver.com','govindarajanv6.mylabserver.com' ]
env.user = 'dummy'
env.key_filename = r'c:\.ssh\id_rsa'

def uptime():
  run('uptime')
