from ModernPhysics.Essentials import Essentials


class Hydrogen(Essentials):

    wavelength = []
    En = []
    dE = []

    def energy_levels(self):
        print("Calculating energy levels of the hydrogen atom")
        n = int(input("Energy level > "))
        En = -13.60/n*n
        print("Energy of state number", n, "is E =", En, " eV")
        store = input("Store this energy instance? (y/n) ")
        if store == 'y':
            self.En.append(self.En)
            print("Instance stored as number ", len(self.En))
        return En

    def transition_wavelength(self):
        print("Wavelength of transition from state ni to nf of the Hydrogen atom")
        ni = int(input("Transitioning from energy state > "))
        nf = int(input("To energy state > "))
        l = (1/self.R)*(ni*ni*nf*nf/(ni**2-nf**2))
        print("Transition wavelength l =", l)
        store = input("Store this wavelength instance? (y/n) ")
        if store == 'Y':
            self.wavelength.append(l)
            print("Instance stored as number ", len(self.wavelength))
        return l

    def transition_energy(self):
        print("Energy of the transition from state ni to nf")
        ni = int(input("Transitioning from energy state > "))
        nf = int(input("To energy state > "))
        l = (1/self.R)*(ni*ni*nf*nf/(ni**2-nf**2))
        dE = self.h*self.c/l
        if dE > 0:
            dE_str = "Absorbed"
        elif dE < 0:
            dE_str = "Given off"
        print("Transition energy dE = ", dE, " ", dE_str)
        store = input("Store this energy instance? (y/n) ")
        if store == 'y':
            self.dE.append(dE)
            print("Instance stored as number ", len(self.dE))
        return dE
