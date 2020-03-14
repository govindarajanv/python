#
number = 23
# input() is used to get input from the user
guess = int(input('Enter an integer : '))

if guess == number:

    print('Congratulations, you guessed it.') # New block starts here

elif guess < number:

    print('No, it is a little higher than that') # Another block

else:

    print('No, it is a little lower than that')

