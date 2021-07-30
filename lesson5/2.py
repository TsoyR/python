class Road:
    def __init__(self,_lenght,_width,volume):
        self.length= _lenght
        self.width= _width
        self.volume=volume
    def formula(self):
        return self.length*self.width*self.volume

a = Road(125,50,20)
print(a.formula())
