# Q1
myTuple=("Red","Green","Blue","White","Orange","Pink","Yellow","Black","Magenta","Brown")

# a. Print the number of item in the tuple (Length).
print(len(myTuple))

# b. Display the item “Blue” by index.
print(myTuple[2])

# c. Display the item “Blue” by negative index.
print(myTuple[-8])

# d. What will be output of print(:4) & also explain it.
print(myTuple[:4])

# e. What will be output of print(4:) & also explain it.
print(myTuple[4:])

# f. Check the tuple for item “Yellow” exists.
if "Yellow" in myTuple:
    print("Item \"Yellow\" exits in the Tuple")
else:
    print("Item does not exits")

# g. Change the tuple item “Orange” to “Santra”
newList=list(myTuple)
newList[4]="Santra"
myTuple=tuple(newList)
print(myTuple)

# h. For check number of times the value 5 appears in given tuple.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 6, 5, 9, 5 )
print("The number of times item 5 occured in the typle is :",thistuple.count(5))

# i. For 'thistuple' Search for the first occurrence of the value 8, and return its position.
print("The index value of the item 8 is :",thistuple.index(8))