# Q4. Write a program to largest among three numbers by creating user defined function.
def largest_Number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 :
        return num2
    else:
        return num3


num1 = 10
num2 = 69
num3 = 27

print(f"{num1}, {num2}, {num3}")
largest = largest_Number(num1, num2, num3)
print(f"Largest numbers is: {largest}")

