
rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30
print(rect.get_perimeter())  # Should print 30




"""
ขอให้เขียนคราส circle ที่ทำงานคล้ายคลึงกับคราส Rectangle พร้อมตัวอย่างการทำงาน
"""

class Circle:
    # ปรับให้ถูกต้องกับความเป็นวงกลม
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area ปรับสูตรพื้นที่วงกลม
    def get_area(self):
        return self.length * self.width

    # Method to get the perimeter ปรับสูตรเส้นรอบวงวงกลม
    def get_perimeter(self):
        return f"Perimeter = {self.length} * {self.width} = {2 * (self.length * self.width)}"


myCircle = Circle(10)
print(myCircle.get_area())
print(myCircle.get_perimeter())