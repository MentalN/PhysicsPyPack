from ModernPhysics.Essentials import Essentials
from scipy.integrate import quad
import math


class OneDWell(Essentials):

    E_n = []
    P_n = []

#   initialized variables for calculating probability
    n = 1
    L = 1

    def energy_infinite_potential(self):
        m = input("Mass of the particle, or type the name of the particle > ")
        try:
            float(m)
        except ValueError:
            if m in self.particles:
                m = self.particles[m]
            else:
                print("Invalid entry!")
                self.energy_infinite_potential()
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
        return E

    def probability_infinite_potential(self):
        print("Probability of finding a particle in infinite potential well")
        self.L = float(input("Length of the well in nm > "))
        self.n = int(input("Energy state > "))
        print("Calculate the probability of finding the particle in the region between ")
        a = float(input("a > "))
        print("and")
        b = float(input("b > "))
        P, prob = quad(self.psi, a, b)
        print("Probability of finding the particle in the defined region P =", P)

    def psi(self, x):
        psi = math.sqrt(2/self.L)*math.sin(self.n*self.pi*x/self.L)
        return psi**2


OneDWell.probability_infinite_potential(OneDWell())







