# Write a program to calculate the factorial of a given number using for loop

num = int(input("Enter number : "))

fact = 1

for i in range(2, num+1):
    fact = fact * i

print(f"The factorial of {num} is {fact}")
# print(f"{num}! = {fact}")