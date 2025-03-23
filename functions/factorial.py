# Q7. Write a program to find factorial of any given number by creating user defined function.
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    
    return fact

number = int(input("Enter the number: "))
print(f"Factorial of the number {number} is: {factorial(number)}")
