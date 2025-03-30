# Q3. Write a program to display element of array by user choice but if user try to
# access element which is out of bound of index then show exception “Your try
# to access the element which is out of range”.

a = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the index number: "))

    print(f"The element at index {index} is: {a[index]}")

except IndexError:
    print("your are trying to access element which is out of bound")

