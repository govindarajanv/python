stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print ("Intial stack is {}".format(stack))

print("Popping the first element")
print ("after pop,{} is removed, contents are {}".format(stack.pop(),stack))
print ("after pop,{} is removed, contents are {}".format(stack.pop(),stack))
print ("after pop,{} is removed, contents are {}".format(stack.pop(),stack))

print ("Final stack is {}".format(stack))