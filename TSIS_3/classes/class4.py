
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(self.x , self.y)
        
    def move(self):
        ff = int(input("Введите новые координаты x:"))
        ss = int(input("Введите новые кординаты y:"))
        self.x = ff
        self.y = ss
        
    def dist(self):
        c = int((self.x ** 2)+(self.y ** 2))
        distance = c ** 0.5
        print(distance)
        
    
        
        
        
x = int(input("Введите кординату x:"))
y = int (input("Введите кординату y:"))
look = Point(x , y)
while 1:
    a = int(input("Введите число 1.Show; 2.Move; 3.dist:"))
    if a == 1:
        look.show()
    if a == 2:
        look.move()
    if a == 3:
        look.dist()
