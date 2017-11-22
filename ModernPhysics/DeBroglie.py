from ModernPhysics.Essentials import Essentials
from ClassicalMechanics.Momentum import LinearMomentum


class Wavelength(Essentials, LinearMomentum):

    deBroglie = []

    def deBroglie_wavelength(self):
        p = input("Momentum. Or type 'calc' to calculate it  > ")
        try:
            float(p)
        except ValueError:
            if p == "calc":
                p = self.p_magnitude()
            else:
                print("Invalid Entry!")
                self.deBroglie_wavelength()
        d_w = self.h/p
        print("DeBroglie Wavelength = ", d_w)
        store = input("Store this wavelength instance? (y/n) ")
        if store == 'y':
            self.deBroglie.append(d_w)
            print("Instance stored as number", len(self.deBroglie))
        return d_w


Wavelength.deBroglie_wavelength(Wavelength())
