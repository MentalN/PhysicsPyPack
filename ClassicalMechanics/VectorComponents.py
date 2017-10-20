# In addition to being a part of the whole PhysicsPyPack project, this script was written to also experiment with
# the idea of making a command line program.

import math


class TwoDimensions:

    def components(self):
        magnitude = float(input('Vector magnitude  > '))
        angle     = float(input('Angle from X-axis in degrees > '))
        vx = magnitude * math.cos(math.radians(angle))
        vy = magnitude * math.sin(math.radians(angle))
        print('X-component =', "%.2f" %vx)
        print('y-component =', "%.2f" %vy)

    def magnitudeGivenComponents(self):
        vx = float(input('x - component > '))
        vy = float(input('y - component > '))
        v  = math.sqrt(vx*vx + vy*vy)
        print('Magnitude =', "%.2f" %v)

    def magnitudeGivenAngle(self):
        vc    = float(input('Component value > '))
        dim   = input('[x], [y]? Given component direction > ')
        angle = float(input('Component angle > '))
        if dim == 'x':
            v = vc / math.cos(math.radians(angle))
        elif dim == 'y':
            v = vc / math.sin(math.radians(angle))
        else:
            print('Direction input error!')
            TwoDimensions.magnitudeGivenAngle(TwoDimensions())
        print('Vector magnitude = ', "%.2f" %v)

    def angleBetween(self):
        vx = float(input("Vector x-component > "))
        vy = float(input("Vector y-component > "))
        theta = math.degrees(math.atan(vy / vx))
        print("Angle between x-component and y-component: ", "%.2f" % theta, "Degrees")
        return theta


class ThreeDimensions:

    def components(self):
        magnitude   = float(input('Vector magnitude  > '))
        azimuth     = float(input('Angle from x-axis in degrees     (Azimuth) > '))
        elevation   = float(input('Angle from xy-plane in degrees (elevation) > '))
        vx = magnitude * math.cos(math.radians(azimuth)) * math.cos(math.radians(elevation))
        vy = magnitude * math.sin(math.radians(azimuth)) * math.cos(math.radians(elevation))
        vz = magnitude * math.sin(math.radians(elevation))
        print('X-component =', "%.2f" %vx)
        print('y-component =', "%.2f" %vy)
        print('z-component =', "%.2f" %vz)

    def magnitudeGivenComponents(self):
        vx = float(input('x - component > '))
        vy = float(input('y - component > '))
        vz = float(input('z - component > '))
        v  = math.sqrt(vx*vx + vy*vy + vz*vz)
        print('Magnitude =', "%.2f" %v)
        return v

    def magnitudeGivenAngle(self):
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
            print('Direction input error!')
            ThreeDimensions.magnitudeGivenAngle(ThreeDimensions())
        print('Vector magnitude = ', "%.2f" %v)
        return v


twod_commands = {"components": TwoDimensions.components,
                 "magnitude given components": TwoDimensions.magnitudeGivenComponents,
                 "magnitude given angle": TwoDimensions.magnitudeGivenAngle,
                 "angle between components": TwoDimensions.angleBetween}

threed_commands = {"components": ThreeDimensions.components,
                   "magnitude given components": ThreeDimensions.magnitudeGivenComponents,
                   "magnitude given angle": ThreeDimensions.magnitudeGivenAngle}


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


menu()
