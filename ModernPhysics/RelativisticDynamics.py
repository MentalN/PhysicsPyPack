import math
from Essentials import Essentials


class Momentum(Essentials):

    p = []

    def momentum(self):
        m = input("Mass > ")
        try:
            float(m)
        except ValueError:
            if m in self.particles:
                m = self.particles[m]
            else:
                print("invalid entry")
                self.momentum()
        v = float(input("Velocity > "))
        b = v/self.c
        p = m*v/math.sqrt(1-b**2)
        print("Momentum p =", p, " kg.m/s")
        store = input("Store this momentum instance? (y/n) ")
        if store == 'y':
            self.p.append(p)
            print("Instance stored as number [", len(self.p), "]")
        return p


class Energy(Essentials):

    Eo = []
    K = []
    Etot = []

    def rest_energy(self):
        m = input("Mass > ")
        try:
            float(m)
        except ValueError:
            if m in self.particles:
                m = self.particles[m]
            else:
                print("invalid entry")
                self.rest_energy()
        Eo = m*self.c**2
        print("Rest energy Eo =", Eo, "J")
        store = input("Store this rest energy instance? (y/n) ")
        if store == 'y':
            self.Eo.append(p)
            print("Instance stored as number [", len(self.Eo), "]")
        return Eo

    def kinetic_energy(self):
        m = input("Mass > ")
        try:
            float(m)
        except ValueError:
            if m in self.particles:
                m = self.particles[m]
            else:
                print("invalid entry!")
                self.rest_energy()
        v = float(input("Velocity > "))
        Eo = m * self.c ** 2
        b = v/self.c
        K = ((m*self.c**2)/math.sqrt(1-b**2))-Eo
        print("Kinetic energy K =", K, "J")
        store = input("Store this Kinetic energy instance? (y/n) ")
        if store == 'y':
            self.K.append(K)
            print("Instance stored as number [", len(self.K), "]")
        return K

    def relativistic_total_energy(self):
        m = input("Mass > ")
        try:
            float(m)
        except ValueError:
            if m in self.particles:
                m = self.particles[m]
            else:
                print("invalid entry!")
                self.rest_energy()
        v = float(input("Velocity > "))
        b = v / self.c
        Etot = ((m * self.c ** 2) / math.sqrt(1 - b ** 2))
        print("Relativistic total energy Etot =", Etot, "J")
        store = input("Store this energy instance? (y/n) ")
        if store == 'y':
            self.Etot.append(Etot)
            print("Instance stored as number [", len(self.Etot), "]")
        return Etot
