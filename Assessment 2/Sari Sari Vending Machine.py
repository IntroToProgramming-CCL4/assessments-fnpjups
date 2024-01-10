#Products Menu
drinks = {                                  # Using a dictionary for the products
    'A1':{'name':'Coke\t\t', 'price': 5},   # \t command to keep the printed output neat and consistent
    'A2':{'name':'Sprite\t\t', 'price': 5},
    'A3':{'name':'M. Dew\t\t', 'price': 6},
    'A4':{'name':'Coffee sachets','price':3},
    'A5':{'name':'Vimto\t\t','price': 4},
    'A6':{'name':'Water\t\t','price': 2},
    'A7':{'name':'Gatorade\t','price': 7},
    'A8':{'name':'C2\t\t\t','price': 6}
}
foods = {
    'B1':{'name':'Stix\t\t', 'price': 8},
    'B2':{'name':'Mr. Krisps\t', 'price': 5},
    'B3':{'name':'Safari (Chips)', 'price': 5},
    'B4':{'name':'Canned Spam\t', 'price': 10},
    'B5':{'name':'Sardines\t', 'price': 8},
    'B6':{'name':'Skyflakes\t', 'price': 7},
    'B7':{'name':'Ritz\t\t', 'price': 5},
    'B8':{'name':'Rice\t\t', 'price': 10}
}
hygiene = {
    'C1':{'name':'Dove Soap bar\t\t', 'price': 3},
    'C2':{'name':'Colgate (toothpaste)', 'price': 3},
    'C3':{'name':'Shampoo sachets\t\t', 'price': 6},
    'C4':{'name':'Conditioner sachets\t', 'price': 6},
    'C5':{'name':'Toothbrush\t\t\t', 'price': 2},
    'C6':{'name':'Body lotion\t\t\t', 'price': 5},
    'C7':{'name':'Perfume\t\t\t\t', 'price': 6},
    'C8':{'name':'Tide pods\t\t\t', 'price': 2}
}
medicine = {
    'D1':{'name':'Panadol (Fevers)\t', 'price': 10},
    'D2':{'name':'Fludrex (Colds)\t\t', 'price': 10},
    'D3':{'name':'Prospan (Cough syrup)', 'price': 15},
    'D4':{'name':'Zyrtec (Colds)\t\t', 'price': 10},
    'D5':{'name':'Strepsils (Cough drops)', 'price': 10}
}
cart = []       # Empty list for to add products into if the user chooses to buy multiple items
import time     # Used to add a few seconds before the next line when called upon

#Function for the categories
def vending_machine():
    print("This vending machine has the following:"
          "\n\tDrinks"
          "\t|\tFoods"
          "\t|\tHygiene"
          "\t\t|\tMedicine\t|")

# Function for adding the prices of multiple products together
def final_cart():
    added_price = 0
    for item in cart:
        for key, value in item.items():
            if key == 'price':
                added_price = added_price + value
    return added_price

# Function that prints the users purchases
def final_purchase():
    for item in cart:
        print(f"Please wait....")
        time.sleep(1)
        print(f"Thank you for buying! your {item['name'].rstrip()} has now been dispensed.")
        time.sleep(.5)

# Function for the receipt
def receipt():
    total_price = final_cart() # Allows us to access the total price of products in the cart
    print("\nPrinting your receipt....")
    time.sleep(2)
    for item in cart:
        print(f"\t{item['name']}\t\t{item['price']} AED") # Accesses the name and price of each item inside the cart and prints it
    print(f"\t\tTotal ---------- {total_price} AED."    # Shows the total price of the products
          f"\nThank you for your purchase, please come again!")

# Function for checkout
def checkout():
    final_price = final_cart()
    try:        # If there is an error in the code this code will skip to except ValueError
        money = float(input(f"Please enter {final_price} AED to purchase your product: "))  # Asks for the user to input their money
        if money == final_price:          # Code for when payment is exact
            final_purchase()
        elif money > final_price:         # Code for when payment is more than required price
            change = money - final_price  # Computes the change
            final_purchase()
            print(f"Your change is {change} AED. Please come again!")
        elif money < final_price:  # Code for when payment is insufficient
            while True:            # Loops until the user inputs the right amount of money
                print("\nThe amount that you have entered is insufficient")  # Tells the user that the money is insufficient
                checkout()
                break
    except ValueError:    # Outcome if the user input is invalid
            print(f"Sorry we do not accept invalid inputs, please enter a proper form of payment.")
            checkout()

# Main function which stores all the needed codes to run the vending machine
def program_run():
    # Functions for the all the menu's
    def drinks_menu():
        for key, item in drinks.items():                                    # Accessing the key and value inside the dictionary
            print(f"{key}\t\t{item['name']}\t\t{item['price']} AED")        # Prints the key and value of every item in the dictionary
    def foods_menu():
        for key, item in foods.items():
            print(f"{key}\t\t{item['name']}\t\t{item['price']} AED")
    def hygiene_menu():
        for key, item in hygiene.items():
            print(f"{key}\t\t{item['name']}\t\t{item['price']} AED")
    def medicine_menu():
        for key, item in medicine.items():
            print(f"{key}\t\t{item['name']}\t\t{item['price']} AED")
    while True: # Allows for the program to loop
        vending_machine()
        buying = True
        continue_buying = True
        while buying:                         # As long as 'buying' is true, the code will loop. Also acts as a filter for valid and invalid inputs
            usr_inpt = input("\nWhat would you like to buy?: ")    # Asks for the user input
            if usr_inpt.title() == 'Drinks':
                drinks_menu()                                      # Will show the menu for drinks
                while continue_buying:
                    drink_input = input("\nPlease enter the code of your desired drink: ")  # Asks the user what drink they want
                    if drink_input.title() in drinks:                                       # Takes the input of the user and prints their desired item
                        order = drinks[drink_input.title()]                                 # Checks if the input is in the dictionary and stores it
                        selected_item = (f"{order['name'].rstrip().title()}"                
                                         f" for {order['price']} AED")          # Accessing and storing the name and price of the selected product
                        cart.append(order)                                                  # Adds the users order into the empty list
                        print(f"{selected_item} added to cart")                             # Tells the user their product was added to the cart
                        continue_buying = False
                        buying = False                                                      # Turn to false in order to stop the code from looping
                    else:                     # Output when the input is invalid
                        print("Please enter a valid code")
                        continue                                    # Will go back to ask the user to input the code of their desired product
            elif usr_inpt.title() == 'Foods':
                foods_menu()
                while continue_buying:
                    food_input = input("\nPlease enter the code of your desired food: ")
                    if food_input.title() in foods:
                        order = foods[food_input.title()]
                        selected_item = (f"{order['name'].rstrip().title()}"
                                         f" for {order['price']} AED")
                        cart.append(order)
                        print(f"{selected_item} added to cart")
                        continue_buying = False
                        buying = False
                    else:
                        print("Please enter a valid code")
                        continue
            elif usr_inpt.title() == "Hygiene":
                hygiene_menu()
                while continue_buying:
                    hygiene_input = input("\nPlease enter the code of your desired hygiene product: ")
                    if hygiene_input.title() in hygiene:
                        order = hygiene[hygiene_input.title()]
                        selected_item = (f"{order['name'].rstrip().title()}"
                                         f" for {order['price']} AED")
                        cart.append(order)
                        print(f"{selected_item} added to cart")
                        continue_buying = False
                        buying = False
                    else:
                        print("Please enter a valid code")
                        continue
            elif usr_inpt.title() == "Medicine":
                medicine_menu()
                while continue_buying:
                    medicine_input = input("\nPlease enter the code of your desired medicine: ")
                    if medicine_input.title() in medicine:
                        order = medicine[medicine_input.title()]
                        selected_item = (f"{order['name'].rstrip().title()}"
                                         f" for {order['price']} AED")
                        cart.append(order)
                        print(f"{selected_item} added to cart")
                        continue_buying = False
                        buying = False
                    else:
                        print("Please enter a valid code")
                        continue
            else:
                print("Please enter a valid category")      # Output when the input is invalid
                continue                                    # Goes back to the start of the program
        break
    option_more = input("\nWould you like to buy more? (Y/N): ")    # Asks the user whether they would like to buy more or proceed to checkout
    if option_more.title() == 'N':
        receipt_input = input("Print a receipt after purchase? (Y/N): ")
        if receipt_input.title() == 'Y':     # If the user chooses to print their receipt, it runs the checkout and receipt function
            checkout()
            time.sleep(1)
            receipt()
        else:                               # Only runs the checkout function
            checkout()
    else:
            print(f"Going back to the menu....\n")
            time.sleep(1)   # Waits for amount of time before executing the next line of code
            program_run()   # Runs the program again

print("\t\t\t\t\t\t\t\t-------------------Welcome to the Sari-Sari Machine!-------------------")      # Greets the user
program_run()   # Runs the entire code
