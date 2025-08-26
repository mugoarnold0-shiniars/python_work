# Dictionary
phonebook ={
    "name": "James Othiambo",
    "phone" : 25474568195,
    "email" : "james@gmail.com",
    "location" : "Westlands",
    "others" : [25475981956 , 25475687980]
}

print("My dictionary of phonebook is:",phonebook)
print(type(phonebook))

# use keys to access the items
print("the name of the person is:",phonebook['name'])
print(phonebook["others"][1])