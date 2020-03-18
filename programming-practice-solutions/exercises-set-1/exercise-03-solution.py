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

#Print all characters starting from 3rd postion till the end
print (name[2:])

#Print all characters till 6th position
print (name[:6])

#Print all characters from 2nd to 4th positions
print (name[1:4])

#print with an index of length  and -(length+1) and see how python reacts to it
print ("length of name:", len(name)) 
#print ("name[length]:",name[len(name)]) #index out of range error
#print ("name[-(length+1)]:",name[-(len(name)+1)]) #index out of range error
print ("name[length]:",name[len(name)-1]) 
print ("name[-(length)]:",name[-(len(name))]) 

#concate string in 3 different ways - using %s, join and +
action = "codes python"
finalString = name + " " + action
print ("Using '+': concatenated string is:",finalString)
print ("Using percentage, concatenated string is:%s %s" % (name,action))
str_list = []
str_list.append(name)
str_list.append(action)
print("using join, concatenated string is: %s" % ''.join(str_list))
