from ModernPhysics.Essentials import Essentials


class EnergyWell(Essentials):

    E_n = []

    def energy_infinite_potential_well(self):
        m = input("Mass of the particle, or type the name of the particle > ")
        try:
            float(m)
        except ValueError:
            if m in self.particles:
                m = self.particles[m]
            else:
                print("Invalid entry!")
                self.energy_infinite_potential_well()
        L = float(input("Length of the region in nm > "))
        L = L*10**-9
        E_o = (self.h**2)/(8*m*L**2)
        n = int(input("Energy state > "))
        E = (n**2)*E_o
        print("Energy of particle in state", n," is E =", E)
        store = input("Store this energy instance? (y/n) ")
        if store == 'y':
            self.E_n.append(E)
            print("Instance stored as number ", len(self.E_n))


EnergyWell.energy_infinite_potential_well(EnergyWell())

