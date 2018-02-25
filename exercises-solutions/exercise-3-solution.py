# Concatenate two strings using both '+' and ','

print ("hi," + "how are you?")
print ("Govind" , "Rajan") #automatic space is added

#Concatenate a string and an integer using '+' and ','
print ("hi," , 5)
print ("hi," + str(5))

#addtion of a string and an integer by converting the string number to integer
print ('8',5)
print (int('8'),5)
print (int('8')+5)

#Find the length of a string
print ("length of the string 'python' is",len("python"))

#Print a string with double quotes in one of the sub strings
print ("I told him \"Bye\"")

# Print a string in a new line character
print ("please enter \n for new line character")

#Print a string with '\n' and escape the same in the next line (don't use 'r')
print ("please enter \\n for new line character")

#Print a string with '\n' and escape the same in the next line (use 'r')
print (r"Please enter \n for new line character")

#Print a string 5 times
print ("Calling out 5 times! " * 5)

#Print the 3 character from the given string
name = "Govindarajan"
print (name[0:3])

#Print the last but one character from the given string
print (name[-2])
