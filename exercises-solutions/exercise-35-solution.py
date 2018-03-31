#convert your python scripts to exe

from cx_Freeze import setup, Executable

setup(name='urlparse', version='0.1', description='Parser',executables= [Executable("distme.py")])


#run python setup.py build 

