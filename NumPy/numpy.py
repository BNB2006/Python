import numpy as np

# Q1. Write a program to create following Array.
#  [[10 20 30 40]
#  [50 60 70 80] ]
arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print("2-D Array :")
print(arr)

# Q2. Write a program to access element 70 using index . 
print()
print("Accesing array element: ",arr[1,2])

# Q3. Write a program to create following Array.
#  [[[11 22 33 44 55]
#  [12 22 32 42 52]]
#  [[13 23 33 43 53]
#  [14 24 34 44 54]]]
arr = np.array([[[11,22,33,44,55],[12,22,32,42,52]],[[13,23,33,43,53],[14,24,34,44,54]]])
print()
print("3-d Array:")
print(arr)

# Q4. Write a program to access element 53 using index. 
print()
print("Accessing 3D array element: ",arr[1,0,4])

# Q5. Write a program to create arr [11,22,33,44,55,66,77,88,99,12,23,34,45] and then slice it from 2nd index to 8th index.
print()
arr = np.array([11,22,33,44,55,66,77,88,99,12,23,34,45])
print("NumPy Array slicing: ",arr[2:8])

# Q6. from Q5 array divide it in 5 parts.
print()
newArray = np.array_split(arr,5)
print("NumPy Array split: ",newArray)

# Q7. Write a program to create array ([11 22 33 44 55], [12 22 32 42 52], [13 23 33 43 53], [14 24 34 44 54]) and then print number of element in each dimension.
print()
arr = np.array([[11,22,33,44,55], [12,22,32,42,52], [13,23,33,43,53], [14,24,34,44,54]])
print("NumPy Array Shape: ",arr.shape)

# Q8. Write a program to create array [11,22,33,44,55,66,77,88,99,12,23,34] and then reshape it in 5 rows and 2 column.
print()
arr = np.array([11,22,33,44,55,66,77,88,99,12,23,34])
newArrray = arr.reshape(4,3)
print("NumPy Array Reshaping:")
print(newArrray)

# Q9. Write a program to create 4 arrays a1=[11 22 33 44 55], a2=[12 22 32 42 52], a3=[13 23 33 43 53]and a4= [14 24 34 44 54]) and then find addition & summation of all 4 arrays.
print()
a1 = np.array([11, 22, 33, 44, 55])
a2 = np.array([12, 22, 32, 42, 52])
a3 = np.array([13, 23, 33, 43, 53])
a4 = np.array([14, 24, 34, 44, 54])

a = np.add(a1,a2)
b = np.add(a3,a4)
print(f"Addtion of all 4 arrays: {np.add(a,b)}")

print("Summation of all 4 arrays: ",np.sum([a1,a2,a3,a4]))


# Q10. then find product of all 4 arrays.
print()
print("product of all 4 array: ",np.prod([a1,a2,a3,a4]))

# Q11. Write a program to create array [5,3,3,4,6,6,7,7,8,9,9] and then find unique element of that array.
print()
arr = np.array([5,3,3,4,6,6])
arr2 = np.array([7,7,8,9,9])
result = np.union1d(arr,arr2)
print("unique values of array :",result)

# Q12. Write a program to create 2 array a1=[11,22,55,77,99] & a2=[22,33,66,77,99] and then find unique values of two arrays.
print()
a1=np.array([11,22,55,77,99])
a2=np.array([22,33,66,77,99])
print("unique values of two arrays :",np.union1d(a1,a2))


# Q13. Write a program to create 2 array a1=[11,22,55,77,99] & a2=[22,33,66,77,99] and then find only the values that are present in both arrays.
print()
a1=[11,22,55,77,99]
a2=[22,33,66,77,99]
print("values that are present in both arrays: ",np.intersect1d(a1,a2))

# Q14. Write a program to create 2 array a1=[11,22,55,77,99] & a2=[22,33,66,77,99] and then find only the values that are present in first array that is not present in second array.
print()
a1=[11,22,55,77,99]
a2=[22,33,66,77,99]
print("values that are present in first array: ",np.setdiff1d(a1, a2, assume_unique=True))