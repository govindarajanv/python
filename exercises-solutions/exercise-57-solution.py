exec ("print('Hello World')")

list_str = "[1,1,1,14,5]"

list_str = exec(list_str)

print (list_str)

exec ("list_str2 = [3,9,4]")
print (list_str2)

#multiline will also work
exec ("def test(): print ('I am inside the method test')")
test()
