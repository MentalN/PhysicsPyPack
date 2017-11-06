import math


class Force:

    k = 8.99 * 10 ** -9
    F = []

    def electrostatic_force_two_particles(self):
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