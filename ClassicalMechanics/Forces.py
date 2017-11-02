import math


class Friction:
    F_s = []
    F_k = []

    def friction_static(self):
        m = float(input("Mass of the object > "))
        F = float(input("Magnitude of force applied on the side of the object > "))
        select = float(input("Plane inclined? (y/n) "))
        if select == 'n':
            f_s = F
        elif select == 'y':
            ang = math.radians(float(input("Angle of the incline in degrees > ")))
            f_s = m * 9.81 * math.sin(ang) - F
        print("Force of the static friction Fs =", "%.2f" % f_s, "N")
        store = input("Store this static force instance? (y/n")
        if store == 'y':
            self.F_s.append(f_s)
            print("Instance stored as number [", len(self.F_s), "]")

    def friction_kinetic(self):
        m = float(input("Mass of the object > "))
        F = float(input("Force applied on the side of the object > "))
        u_k = float(input("Kinetic friction coefficient > "))
        Fk = u_k * m * 9.81
        ax = (F-Fk)/m
