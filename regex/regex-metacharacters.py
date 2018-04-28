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

#metacharacter * means "zero or more repetitions of the previous thing". It tries to match as many repetitions as possible
#matches strings that start with "egg" and follow with zero or more "spam"s
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")

#zero or more number of characters 'a' and '^'
pattern = r"[a^]*"

if re.match(pattern, "aaa"):
   print("Match 1")

if re.match(pattern, "^^^^^^^"):
   print("Match 2")

if re.match(pattern, "eggs"):
   print("Match 3")

#metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more repetitions"
# * matches 0 or more occurrences of the preceding expression.
# + matches 1 or more occurrence of the preceding expression
# ? matches "zero or one repetitions".

pattern= r"g+"
print ("pattern being tested is", pattern)

if re.match(pattern, "g"):
   print("Match 1")

if re.match(pattern, "gggggggggggggg"):
   print("Match 2")

if re.match(pattern, "abc"):
   print("Match 3")

pattern = r"(42)+$"
print ("pattern being tested is", pattern)
if re.match(pattern, "1986"):
    print("Match 1 - contains the pattern")

if re.match(pattern, "424"):
   print("Match 2")

if re.match(pattern, "4242"):
   print("Match 3")

pattern = r"ice(-)?cream"
print ("pattern being tested is", pattern)

if re.match(pattern, "ice-cream"):
   print("Match 1")

if re.match(pattern, "icecream"):
   print("Match 2")

if re.match(pattern, "sausages"):
   print("Match 3")

if re.match(pattern, "ice--ice"):
   print("Match 4")

pattern = r"colo(u)?r"
print ("pattern being tested is", pattern)

if re.match(pattern, "colour"):
   print("colour is matched!!!")

if re.match(pattern, "color"):
   print("color is matched!!!")

# Curly braces can be used to represent the number of repetitions between two numbers
# The regex {x,y} means "between x and y repetitions of something". 
# Hence {0,1} is the same thing as ?.
# '+' is same as {1,}

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")
