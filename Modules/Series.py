# Q3. Write a program to create a module Series having two functions named even and odd. . 
# All functions are parameterised and inputs are taken from user.

def even(number):
    even_List = []
    for i in range (number):
        if i%2==0:
            even_List.append(i)
    return even_List

def odd(number):
    odd_List = []
    for i in range(number):
        if i%2!=0:
            odd_List.append(i)
        
    return odd_List