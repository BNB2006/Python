# Practical: Develop and execute following python program on Regular Expression.
import re

str = "simple is better than complex."

# Q1. Write a program to check if the string starts with "simple" and end with “complex”.
x = re.search("^simple.*complex\\.$", str)
if x:
    print("Yes!, the string Not starts with 'simple' and end with 'complex'")
else:
    print("No, the string Not starts with 'simple' and end with 'complex'")


# Q2. Write a program to search for a sequence that starts with "be", followed exactly 2 (any) characters, and end with "er"
y = re.findall("be.{2}er", str)
print("\nsequence that starts with 'be' and ends with 'er")
print(y)

# Q3. Write a program to search for a sequence that starts with "th", followed by 0 or 1 (any) character, and end with "n"
z = re.findall("th.?n", str)
print("\nsequence that starts with 'th' and ends with 'n'")
print(z)

# Q4. Write a program to replace all “e” characters with the digit “7”.
a = re.sub("e", "7", str)
print("\nAfter replacing all e characters with the digit 7")
print(a)

# Q5. Write a program to find all characters between "e" and "p" in given string.
b = re.findall("[e-p]", str)
print("\nall characters between 'e' and 'p' in given string")
print(b)

# Q6. Write a program to print a list containing all matches to string “ple”
matches = re.findall("ple", str)
print("\na list containing all matches to string 'ple'")
print(matches)