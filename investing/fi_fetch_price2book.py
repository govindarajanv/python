import time
import urllib
from urllib.request import urlopen

goldGrade = ['HDFCBANK.NS','HDFC.NS']
silverGrade = ['GAIL.NS','NMDC.NS'] 

def getStatsFromVR(stock):
    try:
        base_url = "https://www.valueresearchonline.com/stocks/snapshot.asp?code=" + stock
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        request = urllib.request.Request(base_url,headers=headers)
        response = urllib.request.urlopen(request)
        sourceCode = response.read().decode('utf-8')
        #print (sourceCode)

        price_to_book = sourceCode.split("                            P/B: ")[1].split("\r\n")[0]
        stock_name = sourceCode.split("<title> ")[1].split(". - Stock Snapshot - Value Research Online</title>")[0]
        #max_pe = sourceCode.split("\$\('#pb_slider'\).slider")[1].split("min: parseFloat\('")[1].split("\)\,")[0]
        print ("Price to Book Ratio of %s is %s" % (stock_name,price_to_book))
        #print (max_pe)
        
    except Exception as e:
        print ("Failure in the getStatsFromVR method",e)

getStatsFromVR('1459')
