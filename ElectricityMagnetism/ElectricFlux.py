from ElectricityMagnetism.Essentials import Essentials
from math import cos, radians


class Flux(Essentials):

    e_flux = []

    def net_charge(self):
        Q = float(input("Net charge > "))
        phi = Q/self.eps_o
        print("Electric Flux = ", phi)
        store = input("Store this flux instance? (y/n) ")
        if store == 'y':
            self.e_flux.append(phi)
            print("Instance stored as number ", len(self.e_flux))
        return phi

    def electric_field(self):
        E = float(input("Electric Field > "))
        A = float(input("Area > "))
        theta = radians(float(input("Angle > ")))
        phi = E*A*cos(theta)
        print("Electric Flux = ", phi)
        store = input("Store this flux instance? (y/n) ")
        if store == 'y':
            self.e_flux.append(phi)
            print("Instance stored as number ", len(self.e_flux))
        return phi

