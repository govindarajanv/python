import re

# Methods like match, search, finall and sub

pattern = r"spam"

print ("\nFinding \'spam\' in \'eggspamsausagespam\'\n")

print ("Usage of match - exact match as it looks at the beginning of the string")
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

print ("\nFinding \'pam\' in \'eggspamsausages\'\n")
pattern1 = r"pam"
match = re.search(pattern1, "eggspamsausages")
if match:
    # returns string matched
    print(match.group())
    print(match.start())
    print(match.end())
    # positions as tuples
    print(match.span())

str = "My name is David. Hi David."
print ("old string:",str)
pattern = r"David"
newstr = re.sub(pattern, "John", str)
print ("new string:",newstr)
