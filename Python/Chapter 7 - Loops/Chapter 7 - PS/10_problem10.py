#  Write a program to print multiplication table of n using for loops in reversed order

num = int(input("Enter number : "))

print("printing multiplication table in reversed : ")
for i in range(1, 11):
    print(f"{num} X {11 - i} = {num*(11 - i)}")