#Global variable cannot be updated inside a function
x = 6
w = 6

def example():
    print ("executing example function which alters global variable")
    global x
    y = 3
    print ("value of y is ",y)
    print ("Value of global x is ", x)
    print ("x+2=",x+2)
    x+=3
    print ("x+3=", x)
    return x

def better_example():
    #best practice
    print ("executing example function which does not alter global variable")
    global_w = w
    y =3 
    print ("value of y is ",y)
    print ("Value of local copy of global w is ", global_w)
    print ("global_w+2=",global_w+2)
    global_w+=3
    print ("global_w+3=", global_w)
    return global_w

print ("Global variable x has the value of ",x)
print ("Global variable w has the value of ",x)
z = example()
print ("example function returns ",z)
print ("after function call, global variable x has the value of ",x)

z = better_example()
print ("example function returns ",z)
print ("after function call, global variable w has the value of ",w)
