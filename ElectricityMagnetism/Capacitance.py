from ElectricityMagnetism.Essentials import Essentials


class Capacitor(Essentials):

    C = []
    Q = 0
    V = 0
    A = 0
    d = 0

    def __init__(self):
        print("Enter given variables (Case sensitive): ")
        print("Charge (Q) ")
        print("Voltage difference (V) ")
        print("Capacitor Area (A) ")
        print("Distance between plates (d) ")
        var_input = input("> ")
        if var_input == 'Q' or var_input == 'V':
            self.Q = input("Charge > ")
            if self.Q == 'back':
                self.__init__()
            self.V = input("Voltage difference > ")
            if self.V == 'back':
                self.__init__()
            self.given_charge_voltage()
        if var_input == 'A' or var_input == 'd':
            self.A = input("Capacitor area > ")
            if self.A == 'back':
                self.__init__()
            self.d = input("Distance between plates > ")
            if self.d == 'back':
                self.__init__()
            self.given_area_distance()

    def given_charge_voltage(self):
        self.V = float(self.V)
        self.Q = float(self.Q)
        C = self.Q/self.V
        print("Capacitance C = ", C)
        store = input("Store this capacitance instance? (y/n) ")
        if store == 'y':
            self.C.append(C)
            print("Instance store as number ", len(self.C))

    def given_area_distance(self):
        self.A = float(self.A)
        self.d = float(self.d)
        C = self.eps_o*self.A/self.d
        print("Capacitance C = ", C)
        store = input("Store this capacitance instance? (y/n) ")
        if store == 'y':
            self.C.append(C)
            print("Instance store as number ", len(self.C))


