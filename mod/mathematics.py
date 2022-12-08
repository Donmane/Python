import math
class Allmath:
    def __init__(self):
        self.sin()
        self.log()
        self.atan()
        self.cos()
        self.sqrt()
        self.tan()
        self.isfinite()
        self.factorial()
        self.cosh()
        self.log10()
    def sin(self):
        self.num = int(input("Enter your sin:"))
        print(math.sin(self.num))

    def log(self):
        self.num = int(input("Enter your log:"))
        print(math.log(self.num))

    def atan(self):
        self.num = int(input("Enter your atan:"))
        print(math.atan(self.num))
    
    def cos(self):
        self.num = int(input("Enter your cos:"))
        print(math.cos(self.num))

    def sqrt(self):
        self.num = int(input("Enter your squre root:"))
        print(math.sqrt(self.num))

    def tan(self):
        self.num = int(input("Enter your tan:"))
        print(math.tan(self.num))
    
    def isfinite(self):
        self.num = int(input("Enter to check if infinite:"))
        print(math.isfinite(self.num))        
        
    def factorial(self):
        self.num = int(input("Enter to factorial:"))
        print(math.factorial(self.num))        

    def cosh(self):
        self.num = int(input("Enter to hyperbolic cosine:"))
        print(math.cosh(self.num))        
    def log10(self):
        self.num = int(input("Return to base 10:"))
        print(math.log10(self.num))        
ma = Allmath()