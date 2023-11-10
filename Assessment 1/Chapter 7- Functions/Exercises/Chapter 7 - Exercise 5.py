def describe_city(city, country='Armenia'):
    cities = city + " is in " + country + "."
    print(cities) #Code inside the function

describe_city('Yerevan') #Since no value was assigned to the parameter 'country' it will use the default country
describe_city('Budapest','Hungary') #Assigned values will replace the default parameters
describe_city('Armavir')