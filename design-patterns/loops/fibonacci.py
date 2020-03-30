"""
0,1,1,2,3,5,8,13...n
"""
def factorial(n):
    first_value = 0
    second_value = 1
    for i in range(1,n,1):
        if i == 1:
            print ("{} ".format(first_value))
        elif i==2:
            print ("{} ".format(second_value))
        else:
            sum = first_value + second_value
            print ("{} ".format(sum))
            first_value = second_value
            second_value = sum
n=int(input("Enter the number of terms:"))
if n <= 0:
    print ("Enter any number greater than zero")
else:
    factorial(n)
