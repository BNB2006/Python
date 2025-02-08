# Write a program to find wether the given number is prime or not
print("Write a Program to Check Whether a Number Is Prime or Not")
num=int(input("Enter a number :"))
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
if prime:
    print(f"The {num} is Prime number")
else:
    print(f"The {num} is not a prime number")
