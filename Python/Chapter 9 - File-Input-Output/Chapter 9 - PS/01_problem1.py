# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’

f = open("Chapter 9 - PS/Poems.txt")
data = f.read()

if("twinkle" in data):
    print("The word twinkle is exist in content")

else:
    print("The word twinkle does not exist in content")

f.close()