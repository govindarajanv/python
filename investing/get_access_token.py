from urllib2 import urlopen, Request
url = "http://www.morningstar.in/stocks/0p0000cfg9/bse-infosys-ltd/overview.aspx"
token = "my_personal_access_token"

request = Request(url)
request.add_header('Authorization', 'token %s' % token)
response = urlopen(request)
print(response.read())
