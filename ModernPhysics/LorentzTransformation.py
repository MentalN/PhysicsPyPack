import math


class Location:

    c = 299792458
    xl = 0
    yl = 0
    zl = 0
    coords = []

    def __init__(self):
        self.xl = float(input("x-coordinates > "))
        self.yl = float(input("y-coordinates > "))
        self.zl = float(input("z-coordinates > "))

    def transform_coordinate(self):
        u = float(input("Velocity of the object in rest frame > "))
        t = float(input("Time > "))
        b = u/self.c
        r = 1/math.sqrt(1-b**2)
        dim = input("Frame moving in axis (x/y/z) > ")
        if dim == 'x':
            self.xl = (self.xl - u*t)*r
        elif dim == 'y':
            self.yl = (self.yl - u*t)*r
        elif dim == 'z':
            self.zl = (self.zl - u*t)*r
        
        







