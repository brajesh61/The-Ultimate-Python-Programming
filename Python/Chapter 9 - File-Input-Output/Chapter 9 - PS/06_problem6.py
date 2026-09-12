# Write a program to mine a log file and find out whether it contains ‘python’

with open("Chapter 9 - PS/log.txt", "r") as f :
    s = f.read()

if("python" in s):
    print("python word found.")
else:
    print("python word not found.")