# Q4. Write a program to find the given number is even or odd but if user enter 0
# or any character then show exception “Zero is not allowed”.
class ZeroNotAllowed(Exception):
    def __init__(self, message):
        super().__init__(message)
try:
    num = int(input("Enter a number: "))
    if num == 0:
        raise ZeroNotAllowed("Zero not allowed")
    
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

except ZeroNotAllowed as er:
    print(er)