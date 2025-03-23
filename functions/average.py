# Q5. Write a program to find average of two numbers by creating user defined function with return keyword.
def average(num1 ,num2):
    return (num1 + num2)/2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
avg = average(num1, num2)
print(f"Average of {num1} and {num2} is {avg}")