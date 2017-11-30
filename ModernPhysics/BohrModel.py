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


