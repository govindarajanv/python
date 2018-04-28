import re

pattern = r"(.+) \1"
print ("pattern is",pattern)

match = re.match(pattern, "word word")
if match:
   print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2")    

match = re.match(pattern, "abc cde")
if match:
   print ("Match 3")

match = re.match(pattern, "abc ab")
if match:
   print ("Match 4")

match = re.match(pattern, "abc abcd")
if match:
   print ("Match 5")


#  \d, \s, and \w match digits, whitespace, and word characters respectively. 
# In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
# Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. 
# For instance, \D matches anything that isn't a digit

#(\D+\d) matches one or more non-digits followed by a digit.
pattern = r"(\D+\d)"
print ("pattern is",pattern)

match = re.match(pattern, "Hi 999!")
if match:
   print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
   print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")

# The sequences \A and \Z match the beginning and end of a string, respectively. 
# The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
# The sequence \B matches the empty string anywhere else.

pattern = r"\b(cat)\b"
print ("pattern is",pattern)

match = re.search(pattern, "The cat sat!")
if match:
   print ("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
   print ("Match 2")

match = re.search(pattern, "We scattered.")
if match:
   print ("Match 3")
