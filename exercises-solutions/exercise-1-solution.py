#1 printing "Hello World"
print ("Hello World")

#Displaying Python's list of keywords
import keyword
print ("List of key words are ..")
print (keyword.kwlist)

#2 Single and multi line comments
# This is the single line comment
''' This is multiline
    comment, can be
    used for a paragraph '''

#3 Multi line statements
sum = 1+\
      2+\
      3\

print ("sum = ",sum)

#4 mutiple assignments
a,b,c = 1, 2.0, "govindarajanv"

print ("a = ",a)
print ("b = ",b)
print ("c = ",c)

print ("Multiple statements in a line")
#5 multiple statements in a line
a = 3; b=4; c = 5

print ("a = ",a)
print ("b = ",b)
print ("c = ",c)

#print 1,2,3,4 with sep as '|' and end character as '&' default is \n
print (1,2,3,4)
print (1,2,3,4,sep='|',end='&')
print ("")
print ("a",1,"b",2,sep='+',end='=')

#Read input from the user and greet him
print ("Now let us greet and meet")
name = input ("I am Python. May I know your name?")
print ("Hi", name,"!. Glad to meet you!!!")
