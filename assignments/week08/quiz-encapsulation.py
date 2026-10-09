"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class rectangle:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
    def getArea(self):
         return f"Area of {self .width} width and {self.length} = {self.width} * {self.length}"

    def getPerimeter(self):
        return f"Perimeter of {self .width} width and {self.length} = {self.width} * {self.length}"

    def isSquare(self):
        return self.width == self.length
    
myRectangle = rectangle(5,10)

print(myRectangle.getArea())
print(myRectangle.getPerimeter())
print(f"Is square: {myRectangle.isSquare()}")