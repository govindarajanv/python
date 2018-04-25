# To conver $> c:\Python\Python36-32\Tools\scripts\2to3.py 
import urllib.request, urllib.error, urllib.parse

try:
    x = urllib.request.urlopen("http://pythonprogramming.net").read()

    print(x)
except Exception as e:
    print(str(e))
