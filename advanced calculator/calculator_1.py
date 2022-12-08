class mymath:
    def __init__(self):
        pass    
    def add(self, x, y):
        a = x + y
        return a

    def sub(self, x, y):
        a = x-y
        return a

    def mul(self, x, y):
        a = x*y
        return a

    def div(self, x, y):
        a = x/y
        return a

    def mol(self, x, y):
        a = x%y
        return a

    def sqr(self, x):
        a = x**0.5
        return a

    def paul(self,x):
        if x == 1:
            return 1
        else:
            return x * self.paul(x-1)

    def per (self, x, y):
        a = self.paul(x)/self.paul(x-y)
        return a

    def com (self, x, y):
        a = self.paul(x)/self.paul(y) * self.paul(x-y)
        return a
 
