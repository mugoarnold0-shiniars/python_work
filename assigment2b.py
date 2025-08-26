# Inventory
inventory = []
print(inventory)
product1={
    "name" : "Cereals",
    "price" : "10000ksh",
    "quantity" :"550kg",
}
product2 ={
    "name" : "hair gel",
    "price" : "2200ksh",
    "quantity": 50,
}
product3 ={
    "name" : "Oils",
    "price" : "5000ksh",
    "quantity" : "600l",
}

inventory.append(product1)  
inventory.append(product2) 
inventory.append(product3) 

print(inventory)

inventory[0]["price"] = "500ksh"
print(inventory)

