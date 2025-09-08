import numpy as np
from scipy import integrate

def f(x):
    return x**2

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

result, error = integrate.quad(f, a, b)

print("result :", result)
print("error :", error)