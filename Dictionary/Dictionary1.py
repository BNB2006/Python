myDict1 = {
    "Maharashtra": "Mumbai",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Madhya Pradesh": "Bhopal",
    "Karnataka": "Bengaluru",
    "Goa": "Panaji",
}

# Q1
# a. Display the "Goa" value of the given dictionary.
print(myDict1["Goa"])

# b. Change the "Mumbai" value to “Aamchi Mumbai” and display it.
myDict1["Maharashtra"] = "Aamchi Mumbai"
print(myDict1)

# c. Adding two new item “Telangana” : “Hydrabad” and “Andra Pradesh” : “Amrawati” to dictionary.
myDict1.update({"Telangana":"Hydrabad","Andra Pradesh":"Amrawati"})
print(myDict1)

# d. Update the value of “Goa” that is “Panaji” to “Love panji” of dictionary.
myDict1["Goa"]="Love Panji"
print(myDict1)

# e. Remove the “Panjab” : “Chandigarh” item from dictionary.
myDict1.pop("Punjab")
print(myDict1)

# f. Display all key:value pair of dictionary using items() method.
for key, value in myDict1.items():
    print(f"{key}:{value}")

# g. Display all dictionary’s key.
for key in myDict1.keys():
    print(f"{key}")

# h. Display all the values in dictionary.    
for value in myDict1.values():
    print(f"{value}")


