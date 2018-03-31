#readd from a file and output the content into a list
readFile = open('c:\goldGrade_Bfsi.txt','r')
print ("Reading from the file\n")
contents = readFile.readlines()
goldGrade_Bfsi = []
for i in contents:
    goldGrade_Bfsi.append(i.strip('\n'))
print (goldGrade_Bfsi)
print (type(goldGrade_Bfsi))
readFile.close()
