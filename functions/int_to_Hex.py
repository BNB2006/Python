
# Q8. Write a program to Converts an Integer value to Hexadecimal value by using standard library function. 

def int_to_hexadecimal(num):
    hex_value = hex(num)
    return hex_value

num = int(input("\n\nEnter the number: "))
print(f"The hexadecimal value of {num} is: {int_to_hexadecimal(num)}\n\n")