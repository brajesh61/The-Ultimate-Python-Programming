# Write a program to make a copy of a text file “this. txt”

with open("Chapter 9 - PS/this.txt") as f:
    content = f.read()

with open("Chapter 9 - PS/this_copy.txt", "w") as f:
    f.write(content)