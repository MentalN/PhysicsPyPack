from ElectricityMagnetism.Essentials import Essentials
from ElectricityMagnetism.BasicEquations import Current


class Field(Essentials):

    B = []

    def wire_current(self):
        print("Magnetic Field of Current")
        I = input("Current in the wire, or type 'calc' to calculate > ")
        try:
            float(I)
        except ValueError:
            if I == 'calc':
                I = Current()
            else:
                print("Invalid Entry! ")
                self.by_wire_current()
        r = float(input("Radial distance from wire > "))
        B = self.mu_o*I/2*self.pi*r
        print("Magnetic Field B = ", B)
        store = input("Store this magnetic field instance? (y/n)")
        if store == 'y':
            self.B.append(B)
            print("Instance store as number ", len(self.B))
        return B

    def solenoid(self):
        print("Magnetic Field of Solenoid")
        I = input("Current in the wire, or type 'calc' to calculate > ")
        try:
            float(I)
        except ValueError:
            if I == 'calc':
                I = Current()
            else:
                print("Invalid Entry! ")
                self.solenoid()
        L = float(input("Length of Solenoid > "))
        N = float(input("Number of turns > "))
        B = self.mu_o*(N/L)*I
        print("Magnetic Field B = ", B)
        store = input("Store this magnetic field instance? (y/n)")
        if store == 'y':
            self.B.append(B)
            print("Instance store as number ", len(self.B))
        return B

