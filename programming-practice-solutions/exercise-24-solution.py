#os module
import os

pwd = os.getcwd()

print ("current directory",pwd)

#make dir

os.mkdir('testdir')

import time

time.sleep(2)

os.rename('testdir','test_dir')

time.sleep(2)

os.rmdir('test_dir')
