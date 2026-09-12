# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.


class Shape :
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

# Define a derived class called Circle, which inherits from the Shape class
class circle:
    def  __init__(self, radius):
        self.radius = radius

    def area(self):
        return 22/7 * self.radius ** 2
    
    def  perimeter(self):
        return 2 * 22/7 * self.radius

# Define a derived class called tringle, which inherits from the Shape class
class tringle:
    def __init__(self,base,height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 1/2 * self.base * self.height
    
    def perimete(self):
        return self.side1 + self.side2 + self.side3
    
# Define a derived class called rectange, which inherits from the Shape class
class Rectangle:
    def __init__(self, len, wid):
        self.length = len
        self.width = wid

    def area(self):
        return self.length * self.width
    
    def perimieter(self):
        return 2 * (self.length + self.width)


# Example usage
# Create a Circle object with a given radius and calculate its area and perimeter
cir = circle(7) 
print("area of circle :" , cir.area())  
print("perimeter of circle :" , cir.perimeter())   

# Create a Rectangle object with given length and width and calculate its area and perimeter
l = 22
w = 7

Rect = Rectangle(l, w)
print("area of rectangle :" , Rect.area())  
print("perimeter of rectangle :" , Rect.perimieter()) 

# Create a Triangle object with a base, height, and three side lengths, and calculate its area and perimeter
base = 5
height = 4
s1 = 4
s2 = 3
s3 = 5

tri = tringle(base, height, s1,s2,s3)
print("area of tringle : ",tri.area())
print("perimeter of tringle : ",tri.perimete())