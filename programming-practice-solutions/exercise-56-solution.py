#Eval does evaluation, built in function and requires no explicit imports

list_str = "[1,2,3,4,5]"

list_str = eval(list_str)

print (list_str)


x = input("code:")

#enter 5< 3 it automatically evaluates to False 
check_this_out = eval(input("code:"))
print (check_this_out)

