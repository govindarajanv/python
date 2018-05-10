""" 
Create a script that has a single variable you can set at the top called user. This user is a dictionary containing the keys:

'admin' - a boolean representing whether the user is an admin user.
'active' - a boolean representing whether the user is currently active.
'name' - a string that is the users name.
Example:

user = { 'admin': True, 'active': True, 'name': 'Kevin' }
Depending on the values of user print one of the following to the screen when you run the script.

Print (ADMIN) followed by the users name if the user is an admin.
Print ACTIVE - followed by the users name if the user is active.
Print ACTIVE - (ADMIN) followed by the users name if the user is an admin and active.
Print the users name if neither active nor an admin.
Change the values of user and re-run the script multiple times to ensure that it works. 

"""
user = { 'admin': True, 'active': True, 'name': 'Kevin' }

admin_str = ""
final_str = ""
active_str = ""
name = ""

for x,y in user.items():
    if x == 'admin' and y == True:
        admin_str = "ADMIN"
    elif x == 'active' and y == True:
        active_str = "ACTIVE"
    elif x == 'name':
        name = y

if active_str:
    final_str = final_str + active_str
if admin_str:
    final_str = final_str + "-" + admin_str
final_str = final_str + "-" + name
print (final_str)


user = { 'admin': True, 'active': True, 'name': 'Kevin' }
prefix = ""

if user['admin'] and user['active']:
    prefix = "ACTIVE - (ADMIN) "
elif user['admin']:
    prefix = "(ADMIN) "
elif user['active']:
    prefix = "ACTIVE - "

print(prefix + user['name'])
