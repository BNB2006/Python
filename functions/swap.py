
# Q2. Write a program to swapping of two numbers by creating user defined function.
def swap(x,y):
    x=x^y
    y=x^y
    x=x^y
    print(f"After swaping the numbers a={x} and b={y}")

a=10
b=20
print(f"Before swaping hte number a={a} and b={b}")
swap(a,b)
