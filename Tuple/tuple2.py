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
newTuple=myTuple2*2
print(newTuple)

# g. Convert the tuple into a list and add a new item “Workday” to it, then convert it back to a tuple.
newList=list(myTuple2)
newList.append("Workday")
myTuple2=tuple(newList)
print(myTuple2)

# h. For the following tuple remove all occurrences of the value 20 and display the new tuple.
thistuple = (10, 20, 30, 40, 20, 50, 20, 60, 70, 20)
newList=list(thistuple)
for item in newList:
    if item==20:
        newList.remove(item)
thistuple=tuple(newList)
print("After removing 20 :",thistuple)

# i. For the following tuple , find and display the maximum and minimum value.
thistuple = (5, 15, 25, 35, 45, 55, 65, 75, 85, 95)
print("The maximum value in the tuple is :",max(thistuple))
print("The minimum value in the tuple is :",min(thistuple))
