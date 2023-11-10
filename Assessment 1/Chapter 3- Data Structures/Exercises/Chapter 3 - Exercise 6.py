name = ["Russell", "Rey", "Caitlyn", "Francis", "Beryl",] #Names of people to invite
for n in name:
    print("Dear", n, "\nI would like to invite you to dinner on Nov. 23, 2023 at 6:00 PM. \nWe will be eating at my home therefore you are free to choose what you want to wear. \nPlease let me know soon if you would be able to attend. Thank you!\n")

#A guest cannot come to the dinner
print("\nSadly, Beryl will not be able to join us for dinner. Therefore I will invtie Khale instead.\n")
name.remove("Beryl") #Removes Beryl from the list
name.append("Khale") #Adds Khale to the list
for n in name:
    print("Dear", n, "\nI would like to invite you to dinner on Nov. 23, 2023 at 6:00 PM. \nWe will be eating at my home therefore you are free to choose what you want to wear. \nPlease let me know soon if you would be able to attend. Thank you!\n") #Reprint the invites

#Removing guests until 2 is left
print("\nUnfortunately, because the new dinner table I bought will not arrive on time I will only be able to accomodate two guests.\n")

guestR1 = name.pop(2) #guestR means guest removed
print("Sorry", guestR1, "but there is no space at the table for you.")
guestR2 = name.pop(2)
print("Sorry", guestR2, "but there is no space at the table for you.")
guestR3 = name.pop(2)
print("Sorry", guestR3, "but there is no space at the table for you.\n\n")

for n in name:
    print("Dear", n, "you are still invited to the dinner.") #Invite to the last 2 guests

del(name[0])
del(name[0])
#deletes the last two names in the list
print("\n",name) #proof the list is empty