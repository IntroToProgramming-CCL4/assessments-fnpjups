sandwich_orders = ['Ham and cheese','Italian BMT','Grilled cheese','Baloney'] #List of sandwiches
finished_sandwiches = []
while sandwich_orders:
    sandwiches = sandwich_orders.pop() #Takes the sandwiches to put into the empty list
    print("I am making your", sandwiches, "sandwich now.")
    finished_sandwiches.append(sandwiches) #Adds the sandwiches to the empty list
print() #Adds a space in between
for sandwich in finished_sandwiches:
    print("Your", sandwich, "sandwich is done!") #Prints for every element that is in the list