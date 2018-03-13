#file operations

#writing to a file
fileContent="Hello World\nWelcome to file operations"
file = open("sample.txt","w")
file.write(fileContent)
file.close()

#Appending to a file
appendText = "\nThis line is being appended"
file = open("sample.txt",'a')
file.write(appendText)
file.close()

#read from a file and output the content in one shot
readFile = open('sample.txt','r')
print ("Reading from the file\n")
print (readFile.read())
readFile.close()

#read from a file and output the content into a list
readFile = open('sample.txt','r')
print ("Reading from the file\n")
print (readFile.readlines())
readFile.close()
