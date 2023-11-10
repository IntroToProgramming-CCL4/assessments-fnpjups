def make_shirt(size='Large', msg='I love Python'): #set a default value for parameters
    print("\nThis shirts size is", size)
    print("The print on the shirt will be", msg)

make_shirt() #Prints the dedault Parameters
make_shirt('Medium') #Assigned a value for size, default msg
make_shirt('Small','Python is the best!') #Positional Parameters