class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


john = Employee()
john.language = "JavaScript" # This is an instance attribute
print(john.language, john.salary)
 