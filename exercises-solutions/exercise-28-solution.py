import urllib.request
import urllib.parse
import re

url= 'http://pythonprogramming.net'
values = {'s':'basics',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req=urllib.request.Request(url,data)
resp =urllib.request.urlopen(req)
respData = resp.read()
#print (respData)

# . - any character
#* - zero or more references
# ? - one or more references
paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

for each_line in paragraphs:
    print (each_line)
                        
