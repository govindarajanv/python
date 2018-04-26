import re

#Character classes provide a way to match only one of a specific set of characters.
#A character class is created by putting the characters it matches inside square brackets

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
   print("Match 1")

if re.search(pattern, "qwertyuiop"):
   print("Match 2")

if re.search(pattern, "rhythm myths"):
   print("Match 3")

pattern = r"[abc][def]"
if re.search(pattern, "ad"):
   print("Match found for ad")

if re.search(pattern, "ae"):
   print("Match found for ae")

if re.search(pattern, "ea"):
   print("Match found for ea")

#Character classes can also match ranges of characters. 

"""
The class [a-z] matches any lowercase alphabetic character.
The class [G-P] matches any uppercase character from G to P.
The class [0-9] matches any digit. 
Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case
"""
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
   print("Match 1")

if re.search(pattern, "E3"):
   print("Match 2")

if re.search(pattern, "1ab"):
   print("Match 3")

"""
Place a ^ at the start of a character class to invert it. 
This causes it to match any character other than the ones included. 
Other metacharacters such as $ and ., have no meaning within character classes. 
The metacharacter ^ has no meaning unless it is the first character in a class
"""
pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
   print("Match 1")

if re.search(pattern, "AbCdEfG123"):
   print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
   print("Match 3")

if re.search(pattern, "this is all quiet"):
   print("Match 1")

if re.search(pattern, "AbCdEfG123"):
   print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
   print("Match 3")
