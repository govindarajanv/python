"""
1*1*2*3*4*5*6 = 6!
"""

def factorial(n):
    for i in range(0,n+1,1):
        if i==0:
            product  = 1
        elif i==1:
            product  = 1
        else:
            product *= i
    print ("{} ".format(product))
n=int(input("Enter the number for which factorial has to be calculated:"))
if n < 0:
    print ("Enter any number greater than zero")
else:
    factorial(n)


            
