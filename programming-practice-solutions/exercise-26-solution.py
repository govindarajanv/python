import urllib.request
import urllib.parse

#commented ones are for practice
#x = urllib.request.urlopen('https://www.google.com')

#GET call
#print (x.read())

'''
Commenting this part

url = 'http://pythonprogramming.net'
values = {'s':'basic',
          'submit':'search'}


data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

request = urllib.request.Request(url,data)

response = urllib.request.urlopen(request)
responseData = response.read()


print (responseData)

'''
# This throws 403 Forbidden

try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print (x.read())
except Exception as e:
    print (str(e))
    
# We are trying to pass headers to the request and pose as if we are humans not bots

try:
    url = 'https://www.google.com/search?q=test'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    responseData = response.read()
    

    saveFile = open('D:\Code\python\exercises-solutions\withHeaders.txt','w')
    print ("File created")
    saveFile.write(str(responseData))
    saveFile.close()
    
    
except Exception as e:
    print (str(e))
