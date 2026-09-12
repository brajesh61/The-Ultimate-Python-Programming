# Write a program to print the following star pattern. 
# * * * 
# *    *    for n = 3 
# * * *

'''
***
* *  # start and end *
***
'''

num = int(input("Enter number : "))

for i in range(1, num+1):
    if(i == 1 or i == num):
     print("*"*num, end="")
     
    
    else:
       print("*", end="")
       print(" "* (num-2), end="")
       print("*", end="")

    print("")
       

