name = ["Russell", "Rey", "Caitlyn", "Francis", "Beryl",] #Names of people to invite
for n in name:
    print("Dear", n, "\nI would like to invite you to dinner on Nov. 23, 2023 at 6:00 PM. \nWe will be eating at my home therefore you are free to choose what you want to wear. \nPlease let me know soon if you would be able to attend. Thank you!\n")

#A guest cannot come to the dinner
print("\nSadly, Beryl will not be able to join us for dinner. Therefore I will invtie Khale instead.\n")
name.remove("Beryl") #Removes Beryl from the list
name.append("Khale") #Adds Khale to the list
for n in name:
    print("Dear", n, "\nI would like to invite you to dinner on Nov. 23, 2023 at 6:00 PM. \nWe will be eating at my home therefore you are free to choose what you want to wear. \nPlease let me know soon if you would be able to attend. Thank you!\n") #Reprint the invites