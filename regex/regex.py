import re

pattern = r"spam"

print ("\nFinding \'spam\' in \'eggspamsausagespam\'\n")

print ("Usage of match - exact match")
if re.match(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

print ("\nUsage of search - search a given substring in a string and returns the resuult in boolean")
if re.search(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")
    
print ("\nUsage of findall - returns list of substrings matching the pattern")
print(re.findall(pattern, "eggspamsausagespam"))
