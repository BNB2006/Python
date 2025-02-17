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


# Q2
myTuple2 =("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Holiday","Vacation","Weekend")

# a. Print the first and last item of the tuple.
print(myTuple2[0],myTuple2[-1])

# b. Extract and display a sub-tuple containing the first five items.
subTuple=myTuple2[:5]
print(subTuple)

# c. Extract and display a sub-tuple containing the last five items.
subTuple=myTuple2[5:]
print(subTuple)

# d. Reverse the tuple and display it.
newList = list(myTuple2)
newList.reverse()
myTuple2=tuple(newList)
print(myTuple2)

# e. Concatenate this tuple with another tuple and display the result.
extraDays = ("Festival", "Event")
myTuple2+=extraDays
print(myTuple2)

# f. Repeat the tuple twice and display the new tuple.

# g. Convert the tuple into a list and add a new item “Workday” to it, then convert it back to a tuple.
newList=list(myTuple2)
newList.append("Workday")
myTuple2=tuple(newList)
print(myTuple2)

# h. For the following tuple remove all occurrences of the value 20 and display the new tuple.
# thistuple = (10, 20, 30, 40, 20, 50, 20, 60, 70, 20)
# newList = list(thistuple)
# newList = [item for item in newList if item != 20]
# thistuple = tuple(newList)
# print(thistuple)

# i. For the following tuple , find and display the maximum and minimum value.
thistuple = (5, 15, 25, 35, 45, 55, 65, 75, 85, 95)
print("The maximum value in the tuple is :",max(thistuple))
print("The minimum value in the tuple is :",min(thistuple))
