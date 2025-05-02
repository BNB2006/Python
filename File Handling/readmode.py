# # read():
# with open("sample.txt", 'r') as file:
#     content = file.read()
#     print(content)

# # readline():
# with open("sample.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line, end='')
#         line = file.readline()

# readlines():
with open('sample.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
    file.close()