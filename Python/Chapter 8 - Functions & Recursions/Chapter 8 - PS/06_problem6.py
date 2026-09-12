# Write a python function which converts inches to cms

def inchesTocms(Inches):
    cm = Inches * 2.54
    return cm   

cm = int(input("Enter the value in inches : "))
print(f"The corresponding value is {inchesTocms(cm)} cm")
