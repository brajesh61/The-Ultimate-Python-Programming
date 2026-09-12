# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file

with open("Chapter 9 - PS/Donkey.txt", "r") as f :
    content = f.read()

newContent = content.replace("donkey", "#####") 

with open("Chapter 9 - PS/Donkey.txt", "w") as f :
    f.write(newContent)
