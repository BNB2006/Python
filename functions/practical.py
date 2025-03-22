# Practical 8: Develop and execute following python program on User defined functions and standard library function.
# Q1. Write a program to find number is prime or not by creating user defined function.
def isPrime(num):
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    if prime:
        print(f"The {num} is Prime number")
    else:
        print(f"The {num} is not a prime number")

num = int(input("Enter a number :"))
isPrime(num)



# Q2. Write a program to swapping of two numbers by creating user defined function.
def swap(x,y):
    x=x^y
    y=x^y
    x=x^y
    print(f"After swaping the numbers a={x} and b={y}")

a=10
b=20
print(f"before swaping hte number a={a} and b={b}")
swap(a,b)


# Q3. Write a program to reverse the number by creating user defined function and by using standard library function.
def reverse_number_user_defined(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    
    return reverse

def reverse_number_library(num):
    return int(str(num)[::-1])

number = int(input("Enter the number :"))

user_defined = reverse_number_user_defined(number)
print(f"Reversed using user-defined function : {user_defined}")

reverse_library = reverse_number_library(number)
print(f"Reversed using standard library function: {reverse_library}")


# Q4. Write a program to largest among three numbers by creating user defined function.
def largest_Number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 :
        return num2
    else:
        return num3

largest = largest_Number(10, 69, 23)
print(f"Largest numbers is: {largest}")

# Q5. Write a program to find average of two numbers by creating user defined function with return keyword.
def average(num1 ,num2):
    return (num1 + num2)/2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
avg = average(num1, num2)
print(f"Average of {num1} and {num2} is {avg}")

# Q6. Write a program to find roots of quadratic equation by creating user defined function.


# Q7. Write a program to find factorial of any given number by creating user defined function.
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    
    return fact

number = int(input("Enter the number: "))
print(f"Factorial of the number {number} is: {factorial(number)}")


# Q8. Write a program to Converts an Integer value to Hexadecimal value by using standard library function. 
def int_to_hexadecimal(num):
    hex_value = hex(num)
    return hex_value

num = int(input("Enter the number: "))
print(f"The hexadecimal value of {num} is: {int_to_hexadecimal(num)}")