class stringsf():
    def __init__(self, string):
        self.Cgetstring = string
        
    def getstring(self):
        self.Cgetstring = input("Write string: ")
        
    def printstring(self):
        print("Ans: " + self.Cgetstring.upper())
        
inp = stringsf("")

inp.getstring()
inp.printstring()
        
    
        
        