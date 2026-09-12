# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import date
class Person :
    def __init__(self, n, c, birth):
        self.name = n
        self.country = c
        self.DOB = birth
    
    # get age method
    def get_age(self):
        today = date.today()
        age = today.year - self.DOB.year # 2025 - 2000 = 25 
        age -= 1  # 24
        
        #return age
        print("age: ",age,"Years")

p1 = Person("John", "France", date(2000, 12,6))
#print(p1.get_age())
print("name: ",p1.name)
print("Country : ",p1.country)
print("D.O.B : ",p1.DOB)
p1.get_age()

        
