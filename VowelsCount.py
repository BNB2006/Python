#write a program to count how many times "a, e, i, o, u" present in the given string

sentance = '''Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated'''
count=0
for char in sentance:
    if char in 'aeiou':
        count+=1

print(count," aeiou present in the string ")