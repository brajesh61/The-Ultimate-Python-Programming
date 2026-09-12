#Write a program to accept marks of 6 students and display them in a sorted manner

marks = []

st1 = input("Enter marks : ")
marks.append(st1)

st2 = input("Enter marks : ")
marks.append(st2)

st3 = input("Enter marks : ")
marks.append(st3)

st4 = input("Enter marks : ")
marks.append(st4)

st5 = input("Enter marks : ")
marks.append(st5)

st6 = input("Enter marks : ")
marks.append(st6)

marks.sort()

print(marks)