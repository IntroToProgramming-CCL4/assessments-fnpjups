while True: #Code will loop as long as statement is true
    age = input("Enter 'done' when finished.\n\tHow old are you?: ")
    if age == 'done':
        break #This code makes it so that if the user inputs done, the code will stop
    age = int(age) #This allows numbers and integers to be inputted
    if age < 3:
        print("You can get in for free!\n") #Prints if user is less than 3
    elif age < 13:
        print("The ticket costs $10.\n") #Prints if user is less than 13
    else:
        print("The ticket costs $15.\n") #Prints if the input is higher than 13