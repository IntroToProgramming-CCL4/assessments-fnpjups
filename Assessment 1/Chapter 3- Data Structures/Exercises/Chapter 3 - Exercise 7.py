place = ["Niagara Falls", "Baguio", "Japan", "Korea", "Yellowstone National Park", "Armenia"]
print("Original list: ", place, "\n") #Original list
print("Alphabetical order: ", sorted(place)) #Alphabetical Order
print("Original: ", place)
print("\nReverse alphabetical order: ", sorted(place, reverse=True)) #Reverse Alphabetical Order
print("Original: ", place)
place.reverse() #Reverses the list
print("\nReversed list: ", place)
place.reverse()
print("Reversed list back into original: ", place) #Same code to reverse the code back into original list
place.sort() #Permanently sorts the list into alphabetical order
print("\nSorted list: ", place)
place.sort(reverse=True) #reverses the list in alphabetical order
print("Reverse sorted list: ", place)