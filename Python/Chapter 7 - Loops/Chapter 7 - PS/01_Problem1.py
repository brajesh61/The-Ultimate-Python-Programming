# Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter numebr : "))

# print(f"Table of number {num} :")
for i in range(1,11):
     print(f"{num} X {i} = {num * i}")
