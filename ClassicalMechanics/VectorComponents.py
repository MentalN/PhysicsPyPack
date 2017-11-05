# In addition to being a part of the whole PhysicsPyPack project, this script was written to also experiment with
# the idea of making a command line program.

import math


class Vector:

    V_comp = []
    V_mag = []
    Ang = []


class TwoDimensions(Vector):

    def components(self):
        magnitude = float(input('Vector magnitude  > '))
        angle     = float(input('Angle from X-axis in degrees > '))
        vx = magnitude * math.cos(math.radians(angle))
        vy = magnitude * math.sin(math.radians(angle))
        V = [vx, vy]
        print("Vector components: ", V)
        store = input("Store this vector instance? (y/n) ")
        if store == 'y':
            self.V_comp.append(V)
            print("Vector instance stored as number [", len(self.V_comp), "]")
        return V

    def magnitude_given_components(self):
        vx = float(input('x - component > '))
        vy = float(input('y - component > '))
        v  = math.sqrt(vx*vx + vy*vy)
        print('Vector magnitude =', "%.2f" % v)
        store = input("Store this vector magnitude instance? (y/n) ")
        if store == 'y':
            self.V_mag.append(v)
            print("Vector magnitude instance stored as number [", len(self.V_mag), "]")
        return v

    def magnitude_given_angle(self):
        vc    = float(input('Component value > '))
        dim   = input('[x], [y]? Given component direction > ')
        angle = float(input('Component angle in degrees > '))
        if dim == 'x':
            v = vc / math.cos(math.radians(angle))
        elif dim == 'y':
            v = vc / math.sin(math.radians(angle))
        else:
            print('Angle input error!')
            self.magnitude_given_angle()
        print('Vector magnitude = ', "%.2f" % v)
        store = input("Store this vector magnitude instance? (y/n) ")
        if store == 'y':
            self.V_mag.append(v)
            print("Vector magnitude instance stored as number [", len(self.V_mag), "]")
        return v

    def angle_between_components(self):
        vx = float(input("Vector x-component > "))
        vy = float(input("Vector y-component > "))
        theta = math.degrees(math.atan(vy / vx))
        print("Angle between x-component and y-component: ", "%.2f" % theta, "Degrees")
        store = input("Store this angle instance? (y/n) ")
        if store == 'y':
            self.Ang.append(theta)
            print("Angle magnitude instance stored as number [", len(self.Ang), "]")
        return theta


class ThreeDimensions(Vector):

    def components(self):
        magnitude   = float(input('Vector magnitude  > '))
        azimuth     = float(input('Angle from x-axis in degrees     (Azimuth) > '))
        elevation   = float(input('Angle from xy-plane in degrees (elevation) > '))
        vx = magnitude * math.cos(math.radians(azimuth)) * math.cos(math.radians(elevation))
        vy = magnitude * math.sin(math.radians(azimuth)) * math.cos(math.radians(elevation))
        vz = magnitude * math.sin(math.radians(elevation))
        V = [vx, vy, vz]
        print("Vector components: ", V)
        store = input("Store this vector instance? (y/n) ")
        if store == 'y':
            self.V_comp.append(V)
            print("Vector instance stored as number [", len(self.V_comp), "]")
        return V

    def magnitude_given_components(self):
        vx = float(input('x - component > '))
        vy = float(input('y - component > '))
        vz = float(input('z - component > '))
        v  = math.sqrt(vx*vx + vy*vy + vz*vz)
        print('Magnitude =', "%.2f" % v)
        store = input("Store this vector magnitude instance? (y/n) ")
        if store == 'y':
            self.V_mag.append(v)
            print("Vector magnitude instance stored as number [", len(self.V_mag), "]")
        return v

    def magnitude_given_angle(self):
        vc    = float(input('Component value > '))
        dim   = input('x, y, or z? Given component direction > ')
        elevation = float(input('Component elevation angle > '))
        if dim == 'x':
            azimuth = float(input('Component azimuth angle > '))
            v = vc / math.cos(math.radians(azimuth)) * math.cos(math.radians(elevation))
        elif dim == 'y':
            azimuth = float(input('Component azimuth angle > '))
            v = vc / math.sin(math.radians(azimuth)) * math.cos(math.radians(elevation))
        elif dim == 'z':
            v = vc / math.sin(math.radians(elevation))
        else:
            print('Angle input error!')
            self.magnitude_given_angle(ThreeDimensions())
        print('Vector magnitude = ', "%.2f" % v)
        store = input("Store this vector magnitude instance? (y/n) ")
        if store == 'y':
            self.V_mag.append(v)
            print("Vector magnitude instance stored as number [", len(self.V_mag), "]")
        return v


twod_commands = {"components": TwoDimensions.components,
                 "magnitude given components": TwoDimensions.magnitude_given_components,
                 "magnitude given angle": TwoDimensions.magnitude_given_angle,
                 "angle between components": TwoDimensions.angle_between_components}

threed_commands = {"components": ThreeDimensions.components,
                   "magnitude given components": ThreeDimensions.magnitude_given_components,
                   "magnitude given angle": ThreeDimensions.magnitude_given_angle}


def help():
    print("Available commands for both 2D and 3D: ")
    print("> components")
    print("> magnitude given components")
    print("> magnitude given angle")
    print("> angle between components")
    menu()


def menu():
    dim_switch = input("Select dimensions (2D / 3D)  > ")
    if dim_switch == "help":
        help()
    command    = input("Enter calculation command    > ")
    if command == "help":
        help()

    if dim_switch == "2D":
        if command not in twod_commands:
            print("Invalid command! for list of available commands, type in 'help'.")
            menu()
        else:
            twod_commands[command](TwoDimensions())
    elif dim_switch == "3D":
        if command not in threed_commands:
            print("Invalid command! for list of available commands, type in 'help'.")
            menu()
        else:
            threed_commands[command](ThreeDimensions())
    else:
        print("invalid dimensions entry!")
        menu()
    menu()

