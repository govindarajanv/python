#different ways to import a module
# go to python home libs to identify all modules that comes with python
# all third party modules will be there in site packages

# one way
import statistics as stat
#another way
from os import getenv
#third way
from datetime import datetime as d
#fourth way
from math import *

example_list = [4,6,7,8,2,5,8,1]

x = stat.mean(example_list)
print ('mean = ',x)

print ("Env variable of JAVA_HOME is",getenv('JAVA_HOME'))

print ("Today is ",d.today())
