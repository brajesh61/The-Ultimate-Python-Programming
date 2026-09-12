# Write a python function to print multiplication table of a given number

def Table(n):
    i = 1
    while(i<11):
        print(f"{n} X {i} = {n*i}")
        i += 1
    return "Done"
n = int(input("Enter number : "))
# print(Table(n))
Table(n)
