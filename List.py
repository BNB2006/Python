# Q1
mylist = ["Red","Green","Blue","White","Orange","Pink","Ywllow","Black","Magenta","Brown"]

# a:Print the number of list in the list
print(len(mylist))

# b:Display item "orange" by index
print(mylist[4])

# c:Display item "Orange" by negative index
print(mylist[-6])

# d:Display range of items from "White" to "Black"
print(mylist[3:8])

# e:Check the list for item "Yellow" exits
if "Yellow" in mylist:
    print("Yellow exits in list")
else:
    print("Yellow does not exits in list")

#  f:Change the item "Orange" to "Santra"
mylist[4]="Santra"
print(mylist[:])

# g:Add new item "Olive" after "pink"
mylist.insert(6,"Olive")
print(mylist[:])

# h:Add new item "Gold" before "Brown"
mylist.insert(-1,"Gold")
print(mylist)

# i:Remove the item "Blue" by it's index number
mylist.pop(2)
print(mylist)


# Q2
mylist1=["Pasta","Burger","Milk","Egg","Sandwich","Bread","Cream","Beans","Nuts","Rice"]

# i:Display all items of list uisng negative index range
print(mylist1[-10:])

# ii:Display all items in the list from item "Egg"
print(mylist1[3:])

# iii:Append any three new items in the list and display it
mylist1.append("Juice")
mylist1.append("Fruits")
mylist1.append("Curry")
print(mylist1)

# iv:Add another list newlist to mylist1
newlist=["Apple","Banana","Grapes"]
mylist1.extend(newlist)
print(mylist1)

# v:Display the list in ascending order
mylist1.sort()
print(mylist1)

# vi:Display the list in descending order
mylist1.sort(reverse=True)
print(mylist1)