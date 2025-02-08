# Write a program to find the largest number amoung three numbers
a=int(input("Enter the First number : "))
b=int(input("Enter the Second number : "))
c=int(input("Enter the Third number : "))
if a>b and a>c:
    print(a," is Largest number")
elif b>c:
    print(b," is Largest number")
else:
    print(c," is Largest number")