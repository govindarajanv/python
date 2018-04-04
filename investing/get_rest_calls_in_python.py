# importing the required libraries
import json
import requests
 
# api-endpoint
URL = "https://api-global.morningstar.com//sal-service/v1/stock/valuation/v2/0P0000AXIE?access_token=jCPHZLykOCZtb5AldpQExsXL2BiI"
 
head = {"Accept":"applicaiton/json", "Content-type": "application/json", }
	
 
# defining a params dict for the parameters to be sent to the API
cookies = dict(mid='17423110563646529469',Hint='usw2e10')
 
# sending get request and saving the response as response object
r = requests.get(url = URL, headers=head,cookies=cookies,verify=False)
 
# extracting data in json format
data = r.json()
#print (data)
 
 
list_from_json = data['Collapsed']['rows'][0]['datum']
print (len(list_from_json))
price_to_sales = [float(i) for i in list_from_json]
print (sum(price_to_sales[:-3]))
