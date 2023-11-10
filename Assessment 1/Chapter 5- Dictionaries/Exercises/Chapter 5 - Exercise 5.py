pets = [] #Empty list to store the dictionaries in

pet = {'Animal type':'Dog','Name':'Bella','Owner':'Juls'}
pets.append(pet) #This code will add the dictionary into the list
pet = {'Animal type':'Cat','Name':'Diego','Owner':'Yumi'}
pets.append(pet)
pet = {'Animal type':'Pigeon','Name':'Happy','Owner':'Paul'}
pets.append(pet)
for pet in pets:
    print("\nHere's a brief introduction for", pet['Name']+":")
    for key, value in pet.items():  #Code will print for each dictionary(pet) in the list
        print("\n\t" + key + ":", value)