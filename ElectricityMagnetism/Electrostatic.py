from ElectricityMagnetism.Essentials import Essentials


class Coulomb(Essentials):

    F = []
    U = []

    def coulomb_electrostatic_force(self):
        q_1 = float(input("Charge of the first particle > "))
        q_2 = float(input("Charge of the second particles > "))
        r   = float(input("Distance between > "))
        F   = self.k*q_1*q_2/r**2
        print("Electrostatic force between two particles F =", F)
        select = input("Store this electrostatic force instance? (y/n) ")
        if select == 'y':
            self.F.append(F)
            print("Instance stored as number [", len(self.F), "]")
        return F

    def electric_potential_energy_two_charges(self):
        q_1 = float(input("Charge of the first particle > "))
        q_2 = float(input("Charge of the second particles > "))
        r   = float(input("Distance between > "))
        U   = self.k*q_1*q_2/r
        print("Electric potential energy between two particles U =", U)
        select = input("Store this potential energy instance? (y/n) ")
        if select == 'y':
            self.U.append(U)
            print("Instance stored as number [", len(self.U), "]")
        return U

    def electric_potential_energy_n_charges(self):
        n = int(input("Number of charges > "))
        qi = float(input("Charge of the initial particle > "))
        q_sum = 0
        for x in range(n):
            print("Charge of particle [", x+1, "]")
            q = float(input("> "))
            print("Distance from the initial charge > ")
            r = float(input("> "))
            q_sum += q/r
        U = self.k * qi * q_sum
        print("Electric potential energy between two particles U =", U)
        select = input("Store this potential energy instance? (y/n) ")
        if select == 'y':
            self.U.append(U)
            print("Instance stored as number [", len(self.U), "]")
        return








