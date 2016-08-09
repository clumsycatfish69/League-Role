#This imports a module called 'random'
#It allows me to use the random function later in the code
#This website will explain if you want
#https://docs.python.org/2/library/random.html
import random


#All functions begin this way
def rolePick():
    #sets primary to a number 1 through 5
    primary = random.randrange(1,6)
    #creates the variable primaryRole so I can take the number
    #and make it say a role not the number
    primaryRole = ''

    #consecutive if statements that will replace the empty
    #string of primaryRole to the actual name
    if primary == 1:
        primaryRole = 'Top'
    if primary == 2:
        primaryRole = 'Jungle'
    if primary == 3:
        primaryRole = 'Middle'
    if primary == 4:
        primaryRole = 'ADC'
    if primary == 5:
        primaryRole = 'Support'

    #when the function is called it will print the string then the role name
    print('Primary Role: ' + primaryRole)

    #same concept as before but for the secondary role
    secondary = random.randrange(1,6)
    secondaryRole = ''

    #this while loop will keep changing secondary until it
    #does not equal primary
    while secondary == primary:
        secondary = random.randrange(1,6)

    #if statements for secondary, same as above
    if secondary == 1:
        secondaryRole = 'Top'
    if secondary == 2:
        secondaryRole = 'Jungle'
    if secondary == 3:
        secondaryRole = 'Middle'
    if secondary == 4:
        secondaryRole = 'ADC'
    if secondary == 5:
        secondaryRole = 'Support'
    
    print('Secondary Role: ' + secondaryRole)

#"Main" part of code, its where you call functions and such    
#main
#this calls the function and does what is inside the function.
rolePick()

