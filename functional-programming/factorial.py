"""
5! = 5*4*3*2*1*1
0! = 1
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n=int(input("Please enter a number:"))
if n < 0:
    print ("Enter a number greater than zero")
else:
    print ("Factorial of the number {} is {}".format(n,factorial(n)))
