# importing the required libraries
import json
import requests
import statistics
 
# api-endpoint
URL = "https://api-global.morningstar.com/sal-service/v1/stock/valuation/v2/0P0000AXIE?access_token=jCPHZLykOCZtb5AldpQExsXL2BiI"
 
head = {"Accept":"applicaiton/json", "Content-type": "application/json", }
	
 
# defining a params dict for the parameters to be sent to the API
cookies = dict(mid='17423110563646529469',Hint='usw2e10')
 
# sending get request and saving the response as response object
r = requests.get(url = URL, headers=head,cookies=cookies,verify=False)
 
# extracting data in json format
data = r.json()
#print (data)
 
 
list_from_json = data['Collapsed']['rows'][0]['datum']
print (list_from_json)
price_to_sales = [float(i) for i in list_from_json]
print (sum(price_to_sales[:-3]))
print ("Average PS:",statistics.mean(price_to_sales[:-3]))


list_from_json = data['Collapsed']['rows'][1]['datum']
print (list_from_json)
price_to_earning = [float(i) for i in list_from_json]
print (sum(price_to_earning[:-3]))
print ("Average PE:",statistics.mean(price_to_earning[:-3]))
