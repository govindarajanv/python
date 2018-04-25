import urllib.request
import re

def get_quote(symbol):
    base_url = 'https://www.google.com/search?tbm=fin&q=NSE%3A+'

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    request = urllib.request.Request(base_url+symbol,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read()
    print (content)

    #m = re.search(r'id="ref_(.*?)">(.*?)<', content)
    #if m:
        #quote = m.group(2)
    #else:
        #quote = 'no quote available for: ' + symbol
    #return quote
get_quote('PAGEIND')
