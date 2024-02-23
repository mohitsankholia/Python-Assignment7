class Circle:

    def __init__(self):
        radius = int(input("Enter radius : "))
        self.radius = radius

    def calculateArea(self):
        area = 3.14 * self.radius ** 2
        return area

    def calculatePerimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter


obj = Circle()
print("Area of circle will be : ", obj.calculateArea())
print("Perimeter of circle will be : ", format(obj.calculatePerimeter(), ".2f"))