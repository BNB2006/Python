import numpy as np
from scipy.linalg import inv

array1 = np.array([[4, 7],[2, 6]])

A_inverse = inv(array1)

identity_matrix = np.dot(array1, A_inverse)
identity_matrix = np.round(identity_matrix, decimals=5)

print(f"Original Matrix:\n{array1}\n")
print(f"Inverse Matrix:\n{A_inverse}\n")
print(f"array1 * A_inv (Should be Identity Matrix):\n{identity_matrix}\n")