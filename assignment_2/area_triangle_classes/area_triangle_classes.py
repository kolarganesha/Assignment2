'''1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 Function to take the length of the sides of triangle
from user should be defined in the parent class and function to calculate the area should be defined in subclass.'''

class Triangle:
    def __init__(self):
        self.a=None
        self.b=None
        self.c=None

    def len(self):
        self.a = int(input("side 1 :- "))
        self.b = int(input("side 2 :- "))
        self.c = int(input("side 3 :- "))

class Area(Triangle):
    def __init__(self, class_a):
        class_a.len()
        self.var1 = class_a.a
        self.var2 = class_a.b
        self.var3 = class_a.c
    def calcArea(self):
        s = (self.var1 + self.var2 + self.var3)/2
        area = (s * (s - self.var1) * (s - self.var2) * (s - self.var3)) ** 0.5
        return area

t = Triangle()
a = Area(t)
res = a.calcArea()
print(res)

