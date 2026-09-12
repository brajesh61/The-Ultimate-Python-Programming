# Write a program which finds out whether a given name is present in a list or not

Name_list = ["Harry", "Rohan", "Shubham", "Divya"]

name = input("Enter your name: ")

if(name in Name_list):
    print("Your name is in the list")
else:
    print("Your name is not in the list")