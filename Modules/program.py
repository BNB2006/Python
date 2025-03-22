# Practical 9: module Arithmetic

# Q2. Write a program to import above module Arithmetic and call all their functions.

import Arithmetic as ar
import Series as se
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"\nAddition of two numbers is: {ar.add(num1, num2)}\n")
print(f"Subtraction of two numbers is: {ar.sub(num1, num2)}\n")
print(f"Multiplication of two numbers is: {ar.mul(num1, num2)}\n")
print(f"Division of two numbers is: {ar.div(num1, num2)}\n")


# Q4. Write a program to import above module Series and call all their functions. 
series = int(input("Enter the number to print the series: "))
print(f"Even series up to {series}: {se.even(series)}")
print(f"Odd series up to {series}: {se.odd(series)}")

