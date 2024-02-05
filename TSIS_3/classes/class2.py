class Shape():
    def __init__ (self):
        pass
    
    def area(self):
        print("area shape is:" + str(0))
    
class Square():
    def __init__ (self, length):
        self.length = length
        
        
        
    def area(self):
        print("area square is : " + str(self.length ** 2))
        
len = int(input())
SQ = Square(length=len)
SQ.area()
SS = Shape()
SS.area()
