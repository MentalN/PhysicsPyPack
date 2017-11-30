from ModernPhysics.Essentials import Essentials
from periodic.table import element


class Hydrogen(Essentials):

    H_wavelength = []
    H_En = []
    H_dE = []

    def energy_levels(self):
        print("Calculating energy levels of the hydrogen atom")
        n = int(input("Energy level > "))
        En = -13.60/n*n
        print("Energy of state number", n, "is E =", En, " eV")
        store = input("Store this energy instance? (y/n) ")
        if store == 'y':
            self.H_En.append(self.H_En)
            print("Instance stored as number ", len(self.H_En))
        return En

    def transition_wavelength(self):
        print("Wavelength of transition from state ni to nf of the Hydrogen atom")
        ni = int(input("Transitioning from energy state > "))
        nf = int(input("To energy state > "))
        l = (1/self.R)*(ni*ni*nf*nf/(ni**2-nf**2))
        print("Transition wavelength l =", l)
        store = input("Store this wavelength instance? (y/n) ")
        if store == 'Y':
            self.H_wavelength.append(l)
            print("Instance stored as number ", len(self.H_wavelength))
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
            self.H_dE.append(dE)
            print("Instance stored as number ", len(self.H_dE))
        return dE


class Atom(Essentials):

    A_wavelength = []
    A_En = []
    A_dE = []

    def energy_levels(self):
        print("Calculating energy levels of atom with (Z > 1)")
        n = int(input("Energy level > "))
        atom_name = input("Name of the atom > ")
        atom = element(atom_name)
        En = -13.60*(atom.atomic**2)/(n*n)
        print(atom.name, " Energy of state number", n, "is E =", En, " eV")
        store = input("Store this energy instance? (y/n) ")
        if store == 'y':
            self.A_En.append(self.A_En)
            print("Instance stored as number ", len(self.A_En))
        return En

    def transition_energy(self):
        print("Energy of the transition from state ni to nf of non-hydrogen atom")
        atom_name = input("Name of the atom > ")
        atom = element(atom_name)
        ni = int(input("Transitioning from energy state > "))
        nf = int(input("To energy state > "))
        dE = -13.60*(atom.atomic**2)*((1/ni**2)-(1/nf**2))
        if dE > 0:
            dE_str = "Absorbed"
        elif dE < 0:
            dE_str = "Given off"
        print("Transition energy dE = ", dE, " eV ", dE_str)
        store = input("Store this energy instance? (y/n) ")
        if store == 'y':
            self.A_dE.append(dE)
            print("Instance stored as number ", len(self.A_dE))
        return dE

    def transition_wavelength(self):
        print("Wavelength of transition from state ni to nf of non-Hydrogen atom")
        atom_name = input("Name of the atom > ")
        atom = element(atom_name)
        ni = int(input("Transitioning from energy state > "))
        nf = int(input("To energy state > "))
        dE = -13.60*(atom.atomic**2)*((1/ni**2)-(1/nf**2))
        l = self.h*self.c/dE
        print("Transition wavelength l =", l)
        store = input("Store this wavelength instance? (y/n) ")
        if store == 'Y':
            self.A_wavelength.append(l)
            print("Instance stored as number ", len(self.A_wavelength))
        return l


