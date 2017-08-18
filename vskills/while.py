number = 3

running = True
# Error was thrown by Python when indentation was not correct
while running:
    guess = int(input('Enter an integer : '))

    if guess == number:

        print('Congratulations, you guessed it.')

        running = False # this causes the while loop to stop
    
    elif guess < number:

        print('No, it is a little higher than that.')

    else:

        print('No, it is a little lower than that.')

# Remember we have else clause for while loop in python
else:

    print('The while loop is over.')

# Do anything else you want to do here

print('Done')

running = True
while running:
    s = input("Enter any string and \"quit\" for quitting this program : ")
    if s=="quit":
        break
    print ("length of the string is",len(s))
print ("while loop with break is done")
