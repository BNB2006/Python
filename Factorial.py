# Write a program to find Factorial of a given input
num=int(input("Enter a number :"))
factorial=1
if num<0:
    print("The factorial doesn't exist for negetive number")
elif num==0 or num==1:
    print("The facotrial of {num} is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
print(f"The factorial of a {num} is {factorial}")