import json
import requests
import statistics
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
access_token="EEd75l9KHHASq8NQvoGhpiCtaGQl"
stock_code=input("enter the stock code:")
URL = "https://api-global.morningstar.com/sal-service/v1/stock/valuation/v2/" + stock_code +"?access_token="+ access_token
#URL = "https://api-global.morningstar.com/sal-service/v1/stock/valuation/v2/0p0000c0py?access_token="+ access_token
 
head = {"Accept":"applicaiton/json", "Content-type": "application/json", }
        
 
# defining a params dict for the parameters to be sent to the API
cookies = dict(mid='17423110563646529469',Hint='usw2e10')
 
# sending get request and saving the response as response object
r = requests.get(url = URL, headers=head,cookies=cookies,verify=False)
 
# extracting data in json format
data = r.json()
#print (data)
 
 
#####################################################
#   Get Historical Averages
#####################################################

print (data['Collapsed'])
list_from_json = data['Collapsed']['rows'][0]['datum']
print (len(list_from_json))
print ("@@@@@")
print (list_from_json)
#list_from_json = list_from_json[:-3]
price_to_sales = [float(i) for i in list_from_json if i is not None]
print ("price to sales\n");
print (price_to_sales[:-3])
print (sum(price_to_sales[:-3]))
print ("Average PS:",statistics.mean(price_to_sales))
avg_price_to_sales = statistics.mean(price_to_sales)
#
#
list_from_json = data['Collapsed']['rows'][1]['datum']
#print (list_from_json)
price_to_earning = [float(i) for i in list_from_json if i is not None]
print ("price to earnings\n");
print (price_to_earning[:-3])
#print (sum(price_to_earning[:-3]))
print ("Average PE:",statistics.mean(price_to_earning[:-3]))
avg_price_to_earnings = statistics.mean(price_to_earning[:-3])
#
list_from_json = data['Collapsed']['rows'][3]['datum']
#print (list_from_json)
price_to_book = [float(i) for i in list_from_json if i is not None]
print ("price to book\n");
print (price_to_book[:-3])
#print (sum(price_to_book[:-3]))
print ("Average PB:",statistics.mean(price_to_book[:-3]))
avg_price_to_book = statistics.mean(price_to_book[:-3])

#####################################################
#   Get Current Values
#####################################################
current_price_to_sales = price_to_sales[-4]
print ("Current PS:",current_price_to_sales)
current_price_to_earnings = price_to_earning[-4]
print ("Current PE:",current_price_to_earnings)
current_price_to_book = price_to_book[-4]
print ("Current PB:",current_price_to_book)

#####################################################
#   Get Current Values
#####################################################
decision = 'SELL'
possible_upside = 0.00
buy_count = 0
sell_count = 0
if (current_price_to_book <= avg_price_to_book):
    buy_count = buy_count + 1
    decision = 'ACCUMULATE'
    possible_upside = (avg_price_to_book - current_price_to_book)/current_price_to_book *100
    print ("Possible Upside is: ",possible_upside)
else:
    sell_count = sell_count + 1
    possible_upside = 0

if (current_price_to_sales <= avg_price_to_sales):
    buy_count = buy_count + 1
else:
    sell_count = sell_count + 1
if (current_price_to_earnings <= avg_price_to_earnings):
    buy_count = buy_count + 1
else:
    sell_count = sell_count + 1

if (buy_count == 3):
    decision = 'STRONG BUY'
elif (buy_count == 1):
    decision = 'REDUCE'
elif (sell_count == 3):
    decision = 'STRONG SELL'

print ("\n")
print ("Verdict is",decision)
print ("----------------------------------------------------------------\n")

