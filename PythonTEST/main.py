class Circle:
    def __init__(self ,point:tuple , r:int):
        self.point = point
        self.r = r

    def __mul__(self,other):
        return Circle(self.point, self.r * other)
    

    def __str__(self): 
        x,y = self.point
        return f"Center: ({x}; {y}), Radius : {self.r}"
    


circle_1 = Circle((10 , 10) , 30)
circle_2 = circle_1 * 2
print(circle_1)
print(circle_2)