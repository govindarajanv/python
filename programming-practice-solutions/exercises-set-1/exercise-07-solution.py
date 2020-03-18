#functions

#function without any arguments
def greet():
    print ("Hello,Welcome to the world of Python")

# function to get two numbers and add
def perform_addition(num1,num2):
    print ("num1=", num1," num2=", num2)
    answer = num1 + num2
    print ("answer=",answer)

#function with same number but different signature
#This cannot be done in same namespace
#def perform_addition():
#    pass

#function with two default arguments
def perform_addition(num1,num2=4,num3=6):
    print ("num1=", num1," num2=", num2," num3=", num3)
    answer = num1 + num2 + num3
    print ("answer=",answer)

greet()
#perform_addition()

#only last function definition will be used

perform_addition(1,2)
perform_addition(num2=1,num1=2)
perform_addition(1)
perform_addition(1,num3=5)
