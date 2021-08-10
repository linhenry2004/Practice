class Geometric():
    def __init__(self):
        self.color = "Green"
    def getColor(self):
        return self.color
class Circle(Geometric):
    def __init__(self, radius):
        super().__init__()
        self.PI = 3.1415926
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        self.radius = radius
    def getDiameter(self):
        return self.radius * 2
    def getPerimeter(self):
        return self.radius * 2 * self.PI
    def getArea(self):
        return self.PI * (self.radius ** 2)
class Rectangle(Geometric):
    def __init__(self, height, width):
        super().__init__()
        self.height = height
        self.width = width
    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width
    def setHeight(self, height):
        self.height = height
    def setWidth(self, width):
        self.width = width
    def getArea(self):
        return self.height * self.width
    def getPerimeter(self):
        perimeter = 2 * (self.height + self.width)
        return perimeter

def main():
    A = Circle(5)
    print(A.getColor()) #Polymorphism
    print(A.getRadius())
    print(A.getDiameter())
    print(A.getPerimeter())
    print(A.getArea())
    A.setRadius(10)
    print(A.getRadius())
    #isinstance(object, class): Returns true if object belongs to the class
    print(isinstance(A, Circle))
    print(isinstance(A, Geometric))
    print(isinstance(A, Rectangle))

main()
