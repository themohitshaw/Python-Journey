class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def sum(self,another_point):
        return point((self.x + another_point.x) , (self.y + another_point.y))
    
    def print_point(self):
        print( f"x is {self.x} and y is {self.y}")

    def __add__(self, other_point):
        return point((self.x + other_point.x),(self.y + other_point.y))

    def __str__(self):
        print(f"x is {self.x} and y is {self.y}")
    

p1 = point(6,3)
p2 = point(3,2)

result_point = p1.sum(p2)  #Returns a new point which is su of two pints (p1+p2)
result_point.print_point()

p1 = p1+p2   #We overloaded the + operator by writing __add__ function

p1.__str__()
