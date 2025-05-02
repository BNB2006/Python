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


# Q6. Write a program to find roots of quadratic equation by creating user defined function.
