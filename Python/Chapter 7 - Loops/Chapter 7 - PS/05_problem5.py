# Write a program to find the sum of first n natural numbers using while loop

n = int(input("Enter number : "))

sum = 0
i = 1
while(i<=n):
   sum += i
   i += 1

print(f"Sum of 1st {n} numbers = {sum}")
