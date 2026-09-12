# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

s1 = int(input("Enter 1st subject number : "))
s2 = int(input("Enter 2nd subject number : "))
s3 = int(input("Enter 3rd subject number : "))

# total percentage
total_marks = (100*(s1 + s2 + s3))/300


if(total_marks>=40  and s1>=33 and s2>=33 and s3>=33):
    print("Congratutions! You passed : ", total_marks)
    
else:
    print("You failed, try next year :", total_marks)
