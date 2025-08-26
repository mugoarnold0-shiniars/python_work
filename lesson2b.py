# tuple
fruits = ("Bananas","Mango","Grapes","Berries","Apple","Tomato",'Apples')
print("my tuple of fruits is:",fruits)


# note we ca access the items of a tuple by use of the index
print("the first item of the tuple is:",fruits[0])
print("the last item of the tuple is:",fruits[-1])

# slicingofa tuple
print(fruits[2:5])

print(type(fruits))

# note since a tuple is immutable we cannot append an additional fruit at the end
fruits.append("Ovacado")
print(fruits)