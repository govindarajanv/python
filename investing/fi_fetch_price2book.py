import time
import urllib
from urllib.request import urlopen
import re

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
        #print ("Price to Book Ratio of %s is %s" % (stock_name,price_to_book))
        #print (max_pe)
        
    except Exception as e:
        print ("Failure in the getStatsFromVR method",e)
    return stock_name,price_to_book

def max_min_PBV(stock):
    max_pb = 0
    min_pb = 0
    try:
        base_url = "https://www.valueresearchonline.com/stocks/snapshot.asp?code=" + stock
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        request = urllib.request.Request(base_url,headers=headers)
        response = urllib.request.urlopen(request)
        sourceCode = response.read().decode('utf-8')
        #print (sourceCode)

        price_to_book = re.findall(r'<script\s*([^>]*)\s*>(.*?)</script', sourceCode, re.I|re.S)
        java_script_max_pb = price_to_book[39][1]
        max_pb = java_script_max_pb.split(',')[2].strip().split("\'")[1]
        java_script_min_pb = price_to_book[39][1]
        min_pb = java_script_min_pb.split(',')[1].strip().split("\'")[1]
        
    except Exception as e:
        print ("Failure in the max_min_PBV method:%s:%s"%(e, stock))
    return max_pb, min_pb

def max_min_PBV_Others(stock):
    max_pb = 0
    min_pb = 0
    try:
        base_url = "https://www.valueresearchonline.com/stocks/snapshot.asp?code=" + stock
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        request = urllib.request.Request(base_url,headers=headers)
        response = urllib.request.urlopen(request)
        sourceCode = response.read().decode('utf-8')
        #print (sourceCode)

        price_to_book = re.findall(r'<script\s*([^>]*)\s*>(.*?)</script', sourceCode, re.I|re.S)
        java_script_max_pb = price_to_book[36][1]
        max_pb = java_script_max_pb.split(',')[2].strip().split("\'")[1]
        java_script_min_pb = price_to_book[36][1]
        min_pb = java_script_min_pb.split(',')[1].strip().split("\'")[1]
        
    except Exception as e:
        print ("Failure in the max_min_PBV method:%s:%s"%(e,stock))
    return max_pb, min_pb


def getVerdict(pbv,pbv_max, pbv_min):
    #print (pbv)
    current = float(pbv)
    maxval = float(pbv_max)
    minval = float(pbv_min)

    verdict = 'HOLD'
    potential = (0.7 * maxval - current)/current  * 100
    if current <= (1.2 * minval):
        verdict = 'BUY'
    elif current >= (0.7 * maxval):
        verdict = 'SELL'
    else:
        verdict = 'HOLD'

    return verdict,potential

def getListFromFile(filename):

    #read from a file and output the content into a list

    readFile = open(filename,'r')
    contents = readFile.readlines()
    stock_list = []
    for i in contents:
        stock_list.append(i.strip('\n'))
    readFile.close()
    return stock_list

def printVerdict(scrip_list,bfsi_flag=False):
    for i in scrip_list:
        scrip_code = str(i)
        stock,pbv = getStatsFromVR(scrip_code)
        if bfsi_flag == True:
           pbv_max,pbv_min = max_min_PBV(scrip_code)
        else:
           pbv_max,pbv_min = max_min_PBV_Others(scrip_code)
        verdict, potential = getVerdict(pbv,pbv_max, pbv_min)
        if verdict == 'BUY':
            print ("%s: %s with potential upside of %s     pbv_min:%s|pbv:%s|pbv_max:%s" % (stock, verdict, round(potential,2),pbv_min,pbv,pbv_max))


############################################
#  GOLD GRADE STOCKS
############################################
print ("Checking gold standard stocks...\n")

#populate goldGrade_Bfsi
#goldGrade_Bfsi = getListFromFile('c:\goldGrade_Bfsi.txt')
#printVerdict(goldGrade_Bfsi,True)

#populate goldGrade_Others
goldGrade_Others = getListFromFile('c:\goldGrade_Others.txt')
printVerdict(goldGrade_Others)

############################################
#  SILVER GRADE STOCKS
############################################
print ("\n\nChecking silver standard stocks...\n")

#populate silverGrade_Others
#silverGrade_Others = getListFromFile('c:\silverGrade_Others.txt')
#printVerdict(silverGrade_Others)

