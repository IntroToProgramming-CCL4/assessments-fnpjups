rivers = {'Nile':'Egypt','Ganges':'India','Yangtze':'China'} #Three Rivers and Countries where the river is found
for river, country in rivers.items():
    print("The", river, "runs through the country of", country + ".") #This loop will print the river followed by the country where it is located in

print("\nThe rivers are: ")
for river in rivers.keys():
    print("->", river) #Prints the keys of the dictionary (Rivers)

print("\nYou can find these rivers in the countries of: ")
for country in rivers.values():
    print("->", country) #Prints the values of the dictionary (Countries)