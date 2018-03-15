list1 = [5,6,2,8,3,6,8,9,2,34]
print (list1)

#Append a entry to the list
list1.append(7)
print (list1)

#insert at the second location 50
list1.insert(2,50)
print (list1)

#remove first element with value 8 from the list
list1.remove(8)
print (list1)

#remove third element from the list
list1.remove(list1[2])
print (list1)

#print 7th element
print ("seventh element in the list1:",list1[6])

#print elements from 5 to 7
print ("print elements from position 5 to 7:",list1[5:7])

#Access the last element
print ("Last element is ",list1[-1])

#Access the last but one element
print ("Last but one element is ",list1[-2])

print ("Current list is ",list1)
#Get the position of element 3
print ("Position of element 3 is ",list1.index(3))

#get the count of element 2
print ("Total count of element 2:",list1.count(2))

#since list is mutable, copy the list1 into list2 and sort it
list2 = list1
list2.sort()
print (list2)
