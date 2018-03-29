from googlefinance import getQuotes
import time
import json
import os
import sys

def fetchstockquotes(symbol):
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        print( json.dumps(getQuotes(symbol), indent=2))
        time.sleep(5)

symbol=sys.argv[1]
fetchstockquotes(symbol)
