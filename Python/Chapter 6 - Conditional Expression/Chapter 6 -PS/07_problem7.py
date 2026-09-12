# Write a program to find out whether a given post is talking about “John” or not

p1 = input("Enter post : ")

if("john" in p1.lower()):
    print("This post is talking about John.")

else:
    print("This post is not talking about John.")