import math


class Relativistic:
    c = 299792458

    time = []
    mass = []
    length = []

    def time_dilation(self):
        to = float(input("time > "))
        u  = float(input("velocity > "))
        t  = to * (1/math.sqrt(1-(u/self.c)**2))
        print("Dilated time t =", t, "s")
        store = input("Store this time instance? (y/n) ")
        if store == 'y':
            self.time.append(t)
            print("Instance stored as number [", len(self.time), "]")
        return t

    def mass_reduction(self):
        mo = float(input("Mass > "))
        u  = float(input("Velocity > "))
        m  = mo * math.sqrt(1-(u/self.c)**2)
        print("Reduced mass =", m, "kg")
        store = input("Store this mass instance? (y/n) ")
        if store == 'y':
            self.mass.append(m)
            print("Instance stored as number [", len(self.mass), "]")
        return m

    def length_contraction(self):
        Lo = float(input("Proper length > "))
        u  = float(input("Velocity > "))
        L  = Lo * math.sqrt(1-(u/self.c)**2)
        print("Lenght after contraction =", L)
        store = input("Store this length instance? (y/n) ")
        if store == 'y':
            self.mass.append(L)
            print("Instance stored as number [", len(self.length), "]")
        return L


