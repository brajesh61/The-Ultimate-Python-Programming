# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class demo:
    a = 9

b  = demo()
print(b.a)
b.a = 0 # instance atribute
print(b.a) # instance atribute print
print(demo.a) # class atribute is not chnaged. 
