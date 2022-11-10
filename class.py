class MrKola:
    def __init__(self):
        self.name = "Mr kola"
        self.location = "Apata"
        self.mleg = 2
    
    def head(self):
        print(f"{self.name} have one head")
        self.leg()

    def leg(self):
        print(f"{self.name} has {self.mleg} legs")


class Paul(MrKola):
    def __init__(self):
        super().__init__()
        self.name = "paul"
        self.age = 11
        self.head()
    
    def head(self):
        print(f"{self.name} have one head {self.location}")

m= Paul()