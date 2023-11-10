print("What topping do you want on your pizza?")
while True:
    topping = input("Enter your pizza topping. Enter 'quit' when you're done: ") #Asking for user input
    if topping != "quit":
        print("I'll add", topping, "to the pizza!\n") #As long as the statement is true, this code will continue to run until the user inputs 'quit'
    else:
        break #this will run if the user inputs the word 'quit'