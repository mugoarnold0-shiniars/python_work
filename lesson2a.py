# Python list
names = ["Benard","Joylyne","Aaron","Caleb","Arnold","Stephen","Mary"]
print("My list of names is:",names)
print(type(names))
# we can use index to access any name
print(names[1])

# we can use index to access any name
print("the name on the index one is:",names[1])
print("the name on the index five is:",names[5])


counties = ["Mairobi","Mombasa","Isiolo","Kajiado",'Kakamega',"Kisii","Kilifi","Kitui","Kiambu"]


# List slicing
# This is creating a new list from an already existing list by use of imdexes

myCounties  = counties[1:4]
print("My new list is:",myCounties)

print("From the county Kisii to the end:",counties[5:])
print('showing the output upto the third county:',counties[:3])

myCounties =counties[3:6]
print("From the county kajiado all the way to kilifi",myCounties)

# below we see that a lis is mutable
counties[2] = "nandi"
print(counties)

counties[4] = "Turukana"
print(counties)

# pop function is used to remove an item at the list
counties.pop()
print(counties)


# we can use the remove functiom to remove an item of a list
counties.remove("Kilifi")
print(counties)

# we use append function to add an item at the end of the list
counties.append('Kisumu')
print(counties)

counties.sort()
print(counties)

counties.sort(reverse=True)
print(counties)