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
