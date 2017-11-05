class Galilean:

    xg = 0
    yg = 0
    zg = 0
    coords = []

    def transform_coordinates(self):
#       transform x-coordinates
        x_switch = input('Frame moving in x-direction (y/n)? ')
        if x_switch == 'y':
            self.x_transform()
        elif x_switch == 'n':
            self.xg = float(input("x-coordinates > "))
        else:
            print("Invalid entry!")
            self.transform_coordinates()

#       transform y-coordinates
        y_switch = input('Frame moving in y-direction (y/n)? ')
        if y_switch == 'y':
            self.y_transform()
        elif y_switch == 'n':
            self.yg = float(input("y-coordinates > "))
        else:
            print("Invalid entry!")
            self.transform_coordinates()

#       transform z-coordinates
        z_switch = input('Frame moving in z-direction (y/n)? ')
        if z_switch == 'y':
            self.z_transform()
        elif z_switch == 'n':
            self.zg = float(input("z-coordinates > "))
        else:
            print("Invalid entry!")
            self.transform_coordinates()

#       print and store new coordinates
        new_coords = [self.xg, self.yg, self.zg]
        print("Transformed coordinates =", new_coords)
        store = input("Store this new coordinates instance? (y/n) ")
        if store == 'y':
            self.coords.append(new_coords)
            print("Coordinates instance stored as number [", len(self.coords), "]")

    def x_transform(self):
        x  = float(input("x-coordinate > "))
        u  = float(input("Velocity of the frame > "))
        t  = float(input("Time > "))
        self.xg = x - u * t

    def y_transform(self):
        y  = float(input("y-coordinate > "))
        u  = float(input("Velocity of the frame > "))
        t  = float(input("Time > "))
        self.yg = y - u * t

    def z_transform(self):
        z  = float(input("z-coordinate > "))
        u  = float(input("Velocity of the frame > "))
        t  = float(input("Time > "))
        self.zg = z - u * t

