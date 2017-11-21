from Essentials import Essentials


class Photon(Essentials):

    E_photon = []
    P_photon = []
    freq = []

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

    def threshold(self):
        w = input("Value of work function, or enter element symbol > ")
        try:
            float(w)
        except ValueError:
            w = self.work_function(w)
        fo = w/self.h
        lo = self.h*self.c/w
        print("Threshold frequency =", fo)
        print("Corresponding wavelength =", lo)
        store = input("Store this frequency instance? (y/n) ")
        if store == 'y':
            self.freq.append(fo)
            print("Instance stored as number [", len(self.freq), "]")
        return fo

    def work_function(self, wf):
        work_func = {"Al": 4.08, "Be": 5.00, "Cd": 4.07, "Ca": 2.90, "C" : 4.81,
                     "Cs": 2.10, "Co": 5.00, "Cu": 4.70, "Au": 5.10, "Fe": 4.50,
                     "Pb": 4.14, "Mg": 3.68, "Hg": 4.50, "Ni": 5.01, "Nb": 4.30,
                     "K" : 2.30, "Pt": 6.35, "Se": 5.11, "Ag": 4.26, "Na": 2.28,
                     "U" : 3.60, "Zn": 4.30}
        return work_func[wf]

    def excess_energy(self):
        print("Excess energy as kinetic energy")
        w = input("Value of work function, or enter element symbol > ")
        try:
            float(w)
        except ValueError:
            w = self.work_function(w)
        f = input("Frequency, type 'store' to use a stored instance> ")
        try:
            float(f)
        except ValueError:
            if f == 'store':
                num_f = int(input("Number of stored instance > "))
                f = self.freq[num_f]
        k = self.h*f - w
        print("Excess energy K =", k)
        return k
