from math import sqrt


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
        else:
            print("Invalid Entry!")
            self.__init__()

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


class Voltage:

    V = []
    P = 0
    R = 0
    I = 0

    def __init__(self):
        print("Enter given variables (Case sensitive): ")
        print("Power (P) ")
        print("Current (I) ")
        print("Resistance (R) ")
        var_input = input("> ")
        if var_input == 'P':
            print("Enter second variable: ")
            print("Resistance (R) ")
            print("Current (I) ")
            var_input = input("> ")
            if var_input == 'R':
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.given_power_resistance()
            elif var_input == 'I':
                self.I = input("Enter current value > ")
                if self.I == 'back':
                    self.__init__()
                self.given_power_current()
        elif var_input == 'I':
            print("Enter second variable: ")
            print("Power (P) ")
            print("Resistance (R) ")
            var_input = input("> ")
            if var_input == 'P':
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.given_power_current()
            elif var_input == 'R':
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.given_power_resistance()
        elif var_input == 'R':
            print("Enter second variable: ")
            print("Power (P) ")
            print("Current (I) ")
            if var_input == 'P':
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.given_power_resistance()
            elif var_input == 'I':
                self.I = input("Enter current value > ")
                if self.I == 'back':
                    self.__init__()
                self.given_current_resistance()
        else:
            print("Invalid Entry!")
            self.__init__()

    def given_current_resistance(self):
        self.I = float(self.I)
        self.R = float(self.R)
        V = self.I*self.R
        print("Voltage V =", V)
        store = input("Store voltage instance? (y/n) ")
        if store == 'y':
            self.V.append(V)
            print("Instance stored as number ", len(self.V))
        return V

    def given_power_current(self):
        self.P = float(self.P)
        self.I = float(self.I)
        V = self.P/self.I
        print("Voltage V =", V)
        store = input("Store voltage instance? (y/n) ")
        if store == 'y':
            self.V.append(V)
            print("Instance stored as number ", len(self.V))
        return V

    def given_power_resistance(self):
        self.P = float(self.P)
        self.R = float(self.R)
        V =  sqrt(self.P*self.R)
        print("Voltage V =", V)
        store = input("Store voltage instance? (y/n) ")
        if store == 'y':
            self.V.append(V)
            print("Instance stored as number ", len(self.V))
        return V


class Current:

    I = []
    P = 0
    R = 0
    V = 0

    def __init__(self):




    def given_power_resistnace(self):
        self.P = float(self.P)
        self.R = float(self.R)
        I = sqrt(self.P/self.R)
        print("Current I =", I)
        store = input("Store voltage instance? (y/n) ")
        if store == 'y':
            self.I.append(I)
            print("Instance stored as number ", len(self.I))
        return I

    def given_power_voltage(self):
        self.P = float(self.P)
        self.V = float(self.V)
        I = self.P/self.V
        print("Current I =", I)
        store = input("Store voltage instance? (y/n) ")
        if store == 'y':
            self.I.append(I)
            print("Instance stored as number ", len(self.I))
        return I

    def given_voltage_resistance(self):
        self.V = float(self.V)
        self.R = float(self.R)
        I = self.V/self.R
        print("Current I =", I)
        store = input("Store voltage instance? (y/n) ")
        if store == 'y':
            self.I.append(I)
            print("Instance stored as number ", len(self.I))
        return I
