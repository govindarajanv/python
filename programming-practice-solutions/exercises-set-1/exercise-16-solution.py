# tuple does not change, it iterated through faster 
tuple_1 = 1,2,3,4
tuple_2 = (1,2,3,4)
list_1  = [1,2,3,4]

def exampleFunc():
    return 1,2   

x,y = exampleFunc()

print ("first element in tuple 1 ", tuple_1[0])
print ("first element in list_1 ", list_1[0])
