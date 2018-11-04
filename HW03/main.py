import math
class shapes:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def mianji(self):
        return (self.x)*(self.y)
        
class Ellipse(shapes):
    def mianji(self):
        return math.pi*(self.x)*(self.y)
    
class Square(shapes):
    def __init__(self,x):
        self.x=x
    def mianji(self):
        return self.x**2
    
class Ractangle(shapes):
    def mianji(self):
        return (1/2)*(self.x)*(self.y)
class Circle(shapes):
    def __init__(self,x):
        self.x=x
    def mianji(self):
        return math.pi*((self.x)**2)

def compute_area(shapes):
    result=0
    length=len(shapes)
    for i in range(0,length):
        a=shapes[i]
        result+=a.mianji()
    return result
s = [Ellipse(10,20),Square(15),Circle(5),Ractangle(20,15),\
     Circle(5),Square(15),Ellipse(10,20)]
print(compute_area(s))

