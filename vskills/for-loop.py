for i in range(1, 10):

    print(i)

else:

    print('loop#1 ends')

print ("Second for loop with step 2")

for i in range(1, 11, 2):

    print(i)
    

else:

    print('loop#2 ends')

print ("Here 11 will not be included when we mention range as range(1,11,2)")

print ("Printing the list of range")

print (list(range()))
