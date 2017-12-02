class Power:

    P = []
    I = 0
    V = 0
    R = 0

    def __init__(self):
        print("Enter given variables (Case sensitive): ")
        print("Voltage (V) ")
        print("Resistance (R) ")
        print("Current (I) ")
        var_input = input("> ")
        if var_input == 'V':
            print("Enter second variable: ")
            print("Resistance (R) ")
            print("Current (I) ")
            var_input = input("> ")
            if var_input == 'R':
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.given_voltage_resistance()
            elif var_input == 'I':
                self.I = input("Enter Current value > ")
                if self.I == 'back':
                    self.__init__()
                self.given_voltage_current()
        elif var_input == 'R':
            print("Enter second variable: ")
            print("Current (I) ")
            print("Voltage (V) ")
            var_input = input("> ")
            if var_input == 'I':
                self.I = input("Enter current value > ")
                if self.I == 'back':
                    self.__init__()
                self.given_current_resistance()
            elif var_input == 'V':
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.given_voltage_resistance()
        elif var_input == 'I':
            print("Enter second variable: ")
            print("Resistance (R) ")
            print("Voltage (V) ")
            if var_input == 'R':
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.given_current_resistance()
            elif var_input == 'V':
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.given_voltage_current()

    def given_voltage_resistance(self):
        self.V = float(self.V)
        self.R = float(self.R)
        P = self.V**2/self.R
        print("Power P =", P)
        store = input("Store Power instance? (y/n) ")
        if store == 'y':
            self.P.append(P)
            print("Instance stored as number ", len(self.P))
        return P

    def given_voltage_current(self):
        self.V = float(self.V)
        self.I = float(self.I)
        P = self.I*self.V
        print("Power P =", P)
        store = input("Store Power instance? (y/n) ")
        if store == 'y':
            self.P.append(P)
            print("Instance stored as number ", len(self.P))
        return P

    def given_current_resistance(self):
        self.I = float(self.I)
        self.R = float(self.R)
        P = self.I*self.R**2
        print("Power P =", P)
        store = input("Store Power instance? (y/n) ")
        if store == 'y':
            self.P.append(P)
            print("Instance stored as number ", len(self.P))
        return P







