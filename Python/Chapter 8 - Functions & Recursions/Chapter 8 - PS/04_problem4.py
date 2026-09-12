# Write a recursive function to calculate the sum of first n natural numbers

def sumnaturalnum(num):
    s = 0
    for i in range(1, num+1):
        s += i
    return s

num = int(input("Enter number : "))
print(f"Sum of 1st {num} numbers = {sumnaturalnum(num)}")

# 2nd method
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n -1 + n
sum(n) = sum(n-1) + n
'''

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# print(sum(4))