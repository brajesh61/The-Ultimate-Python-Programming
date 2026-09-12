# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle :
    def __init__(self, R):
        self.Radius = R

    # area method
    def area(self):
        return 22/7 * self.Radius ** 2
    
    # area method
    def parimeter(self):
        return 2 * 22/7 * self.Radius

    
cir1 = Circle(7)
print(cir1.area())
print(cir1.parimeter())

