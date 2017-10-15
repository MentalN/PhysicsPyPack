import math

import numpy


class Torque:

    def TorqueMagnitude(self):
        r = float(input("Distance from axis of rotation > "))
        F = float(input("Magnitude of force applied     > "))
        angle = float(input("Angle force is applied at from the lever arm in degrees > "))
        tm = r * F * math.sin(math.radians(angle))
        print("Magnitude of torque =", "%.2f" %tm)

    def TorqueVector(self):
        print("Position vector from the point where the force is applied:")
        rx = float(input("X-component > "))
        ry = float(input("y-component > "))
        rz = float(input("z-component > "))
        r  = [rx, ry, rz]
        print("Force vector: ")
        Fx = float(input("x-component > "))
        Fy = float(input("y-component > "))
        Fz = float(input("z-component > "))
        F  = [Fx, Fy, Fz]
        t = numpy.cross(r, F)
        tm = numpy.linalg.norm(t)
        print("Torque vector: ", t)
        print("Magnitude of torque =", "%.2f" %tm)


def menu():
    print("[1] Torque Magnitude ")
    print("[2] Torque Vector ")
    option = int(input('Select an option > '))

    if option == 1:
        Torque.TorqueMagnitude(Torque())
    elif option == 2:
        Torque.TorqueVector(Torque())
    else:
        print("Invalid Entry!")

    menu()


menu()
