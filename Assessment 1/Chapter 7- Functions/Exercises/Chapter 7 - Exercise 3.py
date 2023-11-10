def make_shirt(size, msg):
    print("This shirts size is", size)
    print("The print on the shirt will be", msg)

make_shirt('Medium',"I like coding") #Positional parameters
print()
make_shirt(size='Small',msg='I like Cats') #Keyword Parameters