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
counter = 1
while running:
    print ("counter =" , counter)
    s = input("Enter any string and \"quit\" for quitting this program : ")
    counter = counter + 1
    if s=="quit":
        break
    if len(s) < 1:
        print ("No number is Entered,loop will end.")
        running = False
    if len(s) < 2:
        print ("Entered number is too small,loop hits continue...")
        continue
    print ("Statement below continue will be skipped if continue is executed")
    print ("length of the string is",len(s))
else:
    print ("second while loop is also over. Else is getting executed as loop has ended. This does not get printed when break condition is met!!!")
