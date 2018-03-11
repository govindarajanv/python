#Get two numbers from user
num1 = input("Enter the first number")
num2 = input ("Enter the second number")
num3 = input ("Enter the third number")

if num1 >= num2:
    if num1 > num3:
        largest = num1
    else:
        largest = num3
elif num2 >= num3:
    largest = num2
else:
    largest = num3

print ("Largest of three numbers %s,%s and %s is %s" % ( num1,num2,num3,largest))
    
    
