import math

class Essentials:

    c = 299792458
    h = 6.62607004e-34
    h_bar = 1.05457180e-34


class Photon(Essentials):

    E_photon = []
    P_photon = []

    def energy(self):
        print("[1} - given frequency > ")
        print("[2} - given wavelength in nm > ")
        given = int(input("Choice number > "))
        if given == 1:
            f = float(input("frequency > "))
            E = self.h*f
        elif given == 2:
            l = float(input("given wavelength in nm > "))
            E = (self.h*self.c)/l
        else:
            print("Invalid entry!")
            self.energy()
        print("Photon energy E =", E)
        store = input("Store this energy instance? (y/n) ")
        if store == 'y':
            self.E_photon.append(E)
            print("Instance stored as number [", len(self.E_photon), "]")
        return E

    def momentum(self):
        print("[1} - given frequency > ")
        print("[2} - given wavelength in nm > ")
        print("[3} - energy > ")
        given = int(input("Choice number > "))
        if given == 1:
            f = float(input("frequency > "))
            P = self.h*f/self.c
        elif given == 2:
            l = float(input("given wavelength in nm > "))
            P = self.h/l
        elif given == 3:
            Ep = input("Photon energy, type 'stored' to use a stored instance > ")
            try:
                float(Ep)
            except ValueError:
                if Ep == "stored":
                    E_num = int(input("Enter number of stored energy instance > "))
                    Ep = self.E_photon[E_num]
                    print("Ep = ", Ep)
                else:
                    print("Invalid Entry!")
                    self.momentum()
            P = Ep/self.c
        else:
            print("Invalid entry!")
            self.momentum()
        print("Photon momentum P =", P)
        store = input("Store this energy instance? (y/n) ")
        if store == 'y':
            self.P_photon.append(P)
            print("Instance stored as number [", len(self.P_photon), "]")
        return P



