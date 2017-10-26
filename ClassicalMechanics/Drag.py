from math import sqrt


class Drag:

    D = []
    v = []
    p = []

    def drag(self):
        A  = float(input("Reference area > "))
        p  = float(input("medium density > "))
        v  = float(input("Velocity > "))
        cd = float(input("Drag coefficient > "))
        D  = cd * (0.5 * p * v * v) * A
        print("Drag Force = ", D," N")
        store = input("Store this drag force instance (y/n)? ")
        if store == 'y':
            Drag.D.append(D)
            print("Drag force instance stored as number:", len(Drag.D))
        return D

    def terminal_velocity(self):
        A  = float(input("Reference area > "))
        m  = float(input("Mass of the object > "))
        cd = float(input("Drag coefficient > "))
        p  = float(input("medium density > "))
        v  = sqrt((2*m*9.81)/cd*p*A)
        print("Terminal velocity =", "%.2f" % v, "m/s")
        store = input("Store this terminal velocity instance (y/n)? ")
        if store == 'y':
            Drag.v.append(v)
            print("Terminal velocity instance stored as number:", len(Drag.v))
        return v

    def air_density(self):
        P = float(input("Absolute pressure (Pa) > "))
        T = float(input("Absolute temperature (K) > "))
#       specific gas constant for dry air in J/kg*K
        R = 287.058
        p = P/R*T
        print("Air density =", "%.2f" % p, " Kg/m3")
        store = input("Store this air density instance (y/n)? ")
        if store == 'y':
            Drag.p.append(p)
            print("Air density instance stored as number:", len(Drag.p))
        return p
