# 1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    
    if(b>a and b>c):
        return b
    
    if(c>a and c>b):
        return c
    
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

print(f"Greatest number is {greatest(a,b,c)}")