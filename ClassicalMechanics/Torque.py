import math

import numpy


class Torque:

    t = []
    t_mag = []

    def torque_magnitude(self):
        r = float(input("Distance from axis of rotation > "))
        F = float(input("Magnitude of force applied     > "))
        angle = float(input("Angle force is applied at from the lever arm in degrees > "))
        tm = r * F * math.sin(math.radians(angle))
        print("Magnitude of torque =", "%.2f" % tm)
        store = input("Store this torque magnitude instant? (y/n) ")
        if store == 'y':
            self.t_mag.append(tm)
            print("Torque instant stored as number [", len(self.t_mag), "]")
        return tm

    def torque_vector(self):
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
        print("Magnitude of torque =", "%.2f" % tm)
        store = input("Store this torque vector instance? (y/n) ")
        if store == 'y':
            self.t.append(t)
            print("Torque instance stored as number [", len(self.t), "]")
        return t


def menu():
    print("[1] Torque Magnitude ")
    print("[2] Torque Vector ")
    option = int(input('Select an option > '))

    if option == 1:
        Torque.torque_magnitude(Torque())
    elif option == 2:
        Torque.torque_vector(Torque())
    else:
        print("Invalid Entry!")

    menu()


