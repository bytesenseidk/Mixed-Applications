from math import hypot

class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    
    def __repr__(self):
        return f"Vector{self.x, self.y}"
    
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    
    def __bool__(self):
        return bool(self.x or self.y)
    
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    vector = Vector(7, 10)
    magnitude = abs(vector)
    scalar_mul = abs(vector * 7)
    print(f"Vector:     {vector}\n"
          f"Magnitude:  {magnitude}\n"
          f"Scaled:     {scalar_mul}")
