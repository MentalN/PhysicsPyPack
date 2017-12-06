from ElectricityMagnetism.Essentials import Essentials


class Field(Essentials):

    E = []
    F = 0
    Q = 0
    d = 0
    V = 0

    def __init__(self):
        print("Enter given variables (Case sensitive): ")
        print("Force (F) ")
        print("Charge (Q)")
        print("Distance (d) ")
        print("Voltage (V) ")
        var_input = input("> ")
        if var_input == 'F':
            self.F = input("Enter force value > ")
            if self.F == 'back':
                self.__init__()
            self.Q = input("Enter charge value > ")
            if self.Q == 'back':
                self.__init__()
            self.given_force_charge()
        elif var_input == 'Q':
            print("Enter second variable: ")
            print("Distance (d) ")
            print("Force (F) ")
            var_input = input("> ")
            if var_input == 'd':
                self.Q = input("Enter charge value > ")
                if self.Q == 'back':
                    self.__init__()
                self.d = input("Enter distance value > ")
                if self.d == 'back':
                    self.__init__()
                self.given_charge_distance()
            elif var_input == 'F':
                self.Q = input("Enter charge value > ")
                if self.Q == 'back':
                    self.__init__()
                self.F = input("Enter force value > ")
                if self.F == 'back':
                    self.__init__()
                self.given_force_charge()
        elif var_input == 'd':
            print("Enter second variable: ")
            print("Charge (Q) ")
            print("Voltage (V) ")
            var_input = input("> ")
            if var_input == 'Q':
                self.d = input("Enter distance value > ")
                if self.d == 'back':
                    self.__init__()
                self.Q = input("Enter charge value > ")
                if self.Q == 'back':
                    self.__init__()
                self.given_charge_distance()
            elif var_input == 'V':
                self.d = input("Enter distance value > ")
                if self.d == 'back':
                    self.__init__()
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.given_voltage_distance()
        elif var_input == 'V':
            self.V = input("Enter Voltage value > ")
            if self.V == 'back':
                self.__init__()
            self.given_voltage_distance()
            self.d = input("Enter distance value > ")
            if self.d == 'back':
                self.__init__()
                self.given_voltage_distance()
        else:
            print("Invalid Entry!")
            self.__init__()

    def given_force_charge(self):
        self.F = float(self.F)
        self.Q = float(self.Q)
        E = self.F/self.Q
        print("Electric Field =", E)
        store = input("Store Electric Field instance? (y/n) ")
        if store == 'y':
            self.E.append(E)
            print("Instance stored as number ", len(self.E))
        return E

    def given_charge_distance(self):
        self.Q = float(self.Q)
        self.d = float(self.d)
        E = self.k*self.Q/self.d**2
        print("Electric Field =", E)
        store = input("Store Electric Field instance? (y/n) ")
        if store == 'y':
            self.E.append(E)
            print("Instance stored as number ", len(self.E))
        return E

    def given_voltage_distance(self):
        self.V = float(self.V)
        self.d = float(self.d)
        E = self.V/self.d
        print("Electric Field =", E)
        store = input("Store Electric Field instance? (y/n) ")
        if store == 'y':
            self.E.append(E)
            print("Instance stored as number ", len(self.E))
        return E