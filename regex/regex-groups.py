import re

#A group can be created by surrounding part of a regular expression with parentheses. 
#This means that a group can be given as an argument to metacharacters such as * and ?.

pattern = r"egg(spam)*"
print ("pattern is",pattern)

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")

pattern = r"([^aeiou][aeiou][^aeiou])"
print ("pattern is",pattern)

if re.match(pattern, "bad"):
   print("Match 1")

if re.match(pattern, "ape"):
   print("Match 2")

if re.match(pattern, "mgm"):
   print("Match 3")

# A call of group(0) or group() returns the whole match. 
# A call of group(n), where n is greater than 0, returns the nth group from the left. 
# The method groups() returns all groups up from 1

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())


# Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. 
# They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.

# Non-capturing groups have the format (?:...). 
# They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())


# '|' means "or", so red|blue matches either "red" or "blue"

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
   print ("Match 1")

match = re.match(pattern, "grey")
if match:
   print ("Match 2")    

match = re.match(pattern, "griy")
if match:
    print ("Match 3")
