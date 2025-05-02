# write() :-
with open('write.txt', 'w') as file:
    file.write("frist line\n")
    file.write("second line\n")
    file.close()

# writelines()
lines = ["First line\n", "Second line\n", "Third line\n"]
with open('write.txt', 'w') as file:
    file.writelines(lines)
    file.close()