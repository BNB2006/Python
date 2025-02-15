student_info = {
 "Name": "John",
 "Age": 20,
 "Course": "Computer Science",
 "Year": 2,
 "Subject": "Math"
}

# a. Print all keys of the dictionary.
for key in student_info.keys():
    print(f"{key}")

# b. Print all values of the dictionary.
for value in student_info.values():
    print(f"{value}")

# c. Retrieve and display the value of the key "Course".
print(student_info["Course"])

# d. Add a new key "Grade" with the value "A" to the dictionary.
student_info.update({"Grade":"A"})
print(student_info)

# e. Update the "Age" key to 21.
student_info["Age"]=21
print(student_info)

# f. Remove the key "Year" from the dictionary and display the updated dictionary.
student_info.pop("Year")
print(student_info)

# g. Check whether the key "Subject" exists in the dictionary.
if "Subject" in student_info.keys():
    print("The Subject key Exits in the Dictionay")
else:
    print("Not Exits")