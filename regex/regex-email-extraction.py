#[\w\.-]+ matches one or more word character, dot or dash.

import re

str = "Please contact info@email.com for assistance"
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
match = re.search(pattern, str)
if match:
   print(match.group())

#In case the string contains multiple email addresses, we could use the re.findall method instead of re.search, to extract all email addresses
str = "Please contact info@email.com or support@email.com for assistance"
match = re.findall(pattern, str)
print (match)
