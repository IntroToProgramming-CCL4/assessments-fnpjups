sandwich_orders = ['Ham and cheese','Pastrami','Italian BLT','Grilled cheese','Pastrami','Baloney','Pastrami'] #List of sandwiches
finished_sandwiches = []

print("I'm sorry, but we currently have no pastrami sandwiches.\n")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami') #Removes all occurences of 'Pastrami' in the list

while sandwich_orders:
    sandwiches = sandwich_orders.pop() #Takes the sandwiches to put into the empty list
    print("I am making your", sandwiches, "sandwich now.")
    finished_sandwiches.append(sandwiches) #Adds the sandwiches to the empty list
print() #Adds a space in between
for sandwich in finished_sandwiches:
    print("Your", sandwich, "sandwich is done!") #Prints for every element that is in the list