class Galilean:

    xg = 0
    yg = 0
    zg = 0

    def inquiry(self):
        x_switch = input('Frame moving in x-direction (y/n)? ')
        if x_switch == 'y':
            Galilean.xTransform(Galilean())
        y_switch = input('Frame moving in y-direction (y/n)? ')
        if y_switch == 'y':
            Galilean.yTransform(Galilean())
        z_switch = input('Frame moving in z-direction (y/n)? ')
        if z_switch == 'y':
            Galilean.zTransform(Galilean())
        Galilean.printNewCoords(Galilean())

    def xTransform(self):
        x  = float(input("x-coordinate > "))
        u  = float(input("Velocity of the frame > "))
        t  = float(input("Time > "))
        Galilean.xg = x - u * t

    def yTransform(self):
        y  = float(input("y-coordinate > "))
        u  = float(input("Velocity of the frame > "))
        t  = float(input("Time > "))
        Galilean.yg = y - u * t

    def zTransform(self):
        z  = float(input("z-coordinate > "))
        u  = float(input("Velocity of the frame > "))
        t  = float(input("Time > "))
        Galilean.zg = z - u * t

    def printNewCoords(self):
        print("Transformed coords:(", "%.2f" %Galilean.xg, ", ", "%.2f" %Galilean.yg, ", ", "%.2f" %Galilean.zg, ")")
        print("Time t is absolute, no transform necessary.")


Galilean.inquiry(Galilean())
