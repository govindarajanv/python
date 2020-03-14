"""
0,1,1,2,3,5,8..
"""

def fibonaaci_series(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fibonaaci_series(n-1)+fibonaaci_series(n-2))

n=int(input("Enter number of terms:"))
if n <= 0:
    print ("Please enter a number greater than 0")
else:
    print("Fibonacci series for {} terms is {}".format(n,fibonaaci_series(n)))
