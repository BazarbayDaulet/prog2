class Rectangle():
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
        
        
    def area(self):
        print(self.lenght * self.width)

a = int(input("Lenght: "))
b = int(input("Width: "))
out = Rectangle(lenght=a, width=b)
out.area()
        