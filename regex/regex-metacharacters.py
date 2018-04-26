import re

# '.' matches any character, other than a new line.
pattern = r"gr.y"
print ("matching the pattern:",pattern)

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "blue"):
   print("Match 3")

pattern = r"^gr.y$"

print ("matching the pattern:",pattern)

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   print("Match 3")
