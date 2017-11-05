from math import sqrt


class Drag:

    D = []
    v = []
    p = []

    def drag(self):
        A  = float(input("Reference area > "))
        p  = input("medium density. To use stored instance type 'stored'. To calculate it instead type 'calc' > ")
        try:
            float(p)
        except ValueError:
            if p == "stored":
                num_p = int(input("Enter number of stored air density instance > "))
                p = self.p[num_p]
            elif p == "calc":
                p = self.air_density()
            else:
                print("Invalid entry!")
                self.drag()
        v  = float(input("Velocity > "))
        cd = input("Drag coefficient, to use 'cd' table type 'shape' > ")
        try:
            float(cd)
        except ValueError:
            if cd == "shape":
                cd = self.cd_table()
            else:
                print("Invalid Entry!")
                self.drag()
        D  = cd * (0.5 * p * v * v) * A
        print("Drag Force = ", D," N")
        store = input("Store this drag force instance (y/n)? ")
        if store == 'y':
            self.D.append(D)
            print("Drag force instance stored as number:", len(self.D))
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
            self.v.append(v)
            print("Terminal velocity instance stored as number:", len(self.v))
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
            self.p.append(p)
            print("Air density instance stored as number:", len(self.p))
        return p

    def cd_table(self):
        print("[1] - Sphere 0.47")
        print("[2] - Half-Sphere 0.42")
        print("[3] - Cone 0.50")
        print("[4] - Cube 1.05")
        print("[5] - Angled Cube 0.80")
        print("[6] - Long Cylinder 0.82")
        print("[7] - Short Cylinder 1.15")
        print("[8] - Streamlined Body 0.045")
        print("[9] - Streamlined Half-body 0.09")
        select = int(input("Enter choice number 1-9 > "))
        if select == 1:
            return 0.47
        elif select == 2:
            return 0.42
        elif select == 3:
            return 0.50
        elif select == 4:
            return 1.05
        elif select == 5:
            return 0.80
        elif select == 6:
            return 0.82
        elif select == 7:
            return 1.15
        elif select == 8:
            return 0.045
        elif select == 9:
            return 0.09
        else:
            print("Invalid entry!")
