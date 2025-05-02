# Q2. Write a program to check whether person eligible for voting or not. If user
# input less than 18 then raise the exception “Your not eligible for voting”
# otherwise print message “Your eligible for voting”. 

class invalidAgeError(Exception):
    def __init__(self, message):
        self.age = age
        self.message = message
        super().__init__(self.message)

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise invalidAgeError("You can not vote")
    
    print("You can vote")

except invalidAgeError as er:
    print(er)

except ValueError:
    print("Invalid input! Please enter a valid age.")


