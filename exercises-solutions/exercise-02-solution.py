import math
#Get two numbers as input 

print ("\n")
num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
print ("\n")

#Adding those numbers
print ("Addition of %d and %d = %d\n" % (num1,num2, num1+num2))

#Subtracting those numbers
print ("Subtraction of %d and %d = %d\n" % (num1,num2, num1-num2))

#Multiplying those numbers
print ("Multiplication of %d and %d = %d\n" % (num1,num2, num1*num2))

#Dividing those numbers
print ("Division of %d and %d = %d\n" % (num1,num2, num1/num2))

#Divide and get only ceil of the number
print ("Ceil of Division of %d and %d = %d\n" % (num1,num2, math.ceil(num1/num2)))

#Find Modulus
print ("Modulus of %d and %d = %d\n" % (num1,num2, (num1%num2)))

# first number to power of second number
print ("%d to the power of %d = %d\n" % (num1,num2, (num1 ** num2)))
