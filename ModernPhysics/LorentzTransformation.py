import math


class Location:

    c = 299792458
    xl = 0
    yl = 0
    zl = 0
    tl = 0
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
            self.tl = r * (t - u*self.xl/self.c**2)
            self.xl = (self.xl - u*t)*r
        elif dim == 'y':
            self.tl = r * (t - u*self.yl/self.c**2)
            self.yl = (self.yl - u*t)*r
        elif dim == 'z':
            self.tl = r * (t - u*self.zl/self.c**2)
            self.zl = (self.zl - u*t)*r
        else:
            print("Invalid entry!")
            self.transform_coordinate()
        new_coords = [self.xl, self.yl, self.zl, self.tl]
        print("New transformed coordinates: ", new_coords)
        store = input("Save this new coordinates instance? (y/n) ")
        if store == 'y':
            self.coords.append(new_coords)
            print("Coordinates saved as instance number: ", len(self.coords))







