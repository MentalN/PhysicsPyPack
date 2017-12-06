from math import sqrt


class Power:

    P = []
    I = 0
    V = 0
    R = 0

    def __init__(self):
        print("Power Equations")
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
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.given_voltage_resistance()
            elif var_input == 'I':
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
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
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.I = input("Enter current value > ")
                if self.I == 'back':
                    self.__init__()
                self.given_current_resistance()
            elif var_input == 'V':
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.given_voltage_resistance()
        elif var_input == 'I':
            print("Enter second variable: ")
            print("Resistance (R) ")
            print("Voltage (V) ")
            if var_input == 'R':
                self.I = input("Enter Current value > ")
                if self.I == 'back':
                    self.__init__()
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.given_current_resistance()
            elif var_input == 'V':
                self.I = input("Enter Current value > ")
                if self.I == 'back':
                    self.__init__()
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
        print("Voltage Equations")
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
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.given_power_resistance()
            elif var_input == 'I':
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
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
                self.I = input("Enter current value > ")
                if self.I == 'back':
                    self.__init__()
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.given_power_current()
            elif var_input == 'R':
                self.I = input("Enter current value > ")
                if self.I == 'back':
                    self.__init__()
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.given_power_resistance()
        elif var_input == 'R':
            print("Enter second variable: ")
            print("Power (P) ")
            print("Current (I) ")
            if var_input == 'P':
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.given_power_resistance()
            elif var_input == 'I':
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
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
        print("Current Equations")
        print("Enter given variables (Case sensitive): ")
        print("Power (P) ")
        print("Resistance (R) ")
        print("Voltage (V) ")
        var_input = input("> ")
        if var_input == 'P':
            print("Enter second variable: ")
            print("Resistance (R) ")
            print("Voltage (V) ")
            var_input = input("> ")
            if var_input == 'R':
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.given_power_resistance()
            elif var_input == 'V':
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
            self.given_power_voltage()
        elif var_input == 'R':
            print("Enter second variable: ")
            print("Power (P) ")
            print("Voltage (V) ")
            var_input = input("> ")
            if var_input == 'P':
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.given_power_resistance()
            elif var_input == 'V':
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.given_voltage_resistance()
        elif var_input == 'V':
            print("Enter second variable: ")
            print("Power (P) ")
            print("Resistance (R) ")
            var_input = input("> ")
            if var_input == 'P':
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.given_power_voltage()
            elif var_input == 'R':
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.R = input("Enter Resistance value > ")
                if self.R == 'back':
                    self.__init__()
                self.given_voltage_resistance()
        else:
            print("Invalid Entry!")
            self.__init__()

    def given_power_resistance(self):
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


class Resistance:

    R = []
    P = 0
    I = 0
    V = 0

    def __init__(self):
        print("Resistance Equations")
        print("Enter given variables (Case sensitive): ")
        print("Power (P) ")
        print("Current (I) ")
        print("Voltage (V) ")
        var_input = input("> ")
        if var_input == 'P':
            print("Enter second variable: ")
            print("Current (I) ")
            print("Voltage (V) ")
            var_input = input("> ")
            if var_input == 'I':
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.I = input("Enter current value > ")
                if self.I == 'back':
                    self.__init__()
                self.given_power_current()
            elif var_input == 'V':
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.given_voltage_power()
        elif var_input == 'I':
            print("Enter second variable: ")
            print("Power (P) ")
            print("Voltage (V) ")
            var_input = input("> ")
            if var_input == 'P':
                self.I = input("Enter current value > ")
                if self.I == 'back':
                    self.__init__()
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.given_power_current()
            elif var_input == 'V':
                self.I = input("Enter current value > ")
                if self.I == 'back':
                    self.__init__()
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.given_voltage_current()
        elif var_input == 'V':
            print("Enter second variable: ")
            print("Power (P) ")
            print("Current (I) ")
            var_input = input("> ")
            if var_input == 'P':
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.P = input("Enter power value > ")
                if self.P == 'back':
                    self.__init__()
                self.given_voltage_power()
            elif var_input == 'I':
                self.V = input("Enter Voltage value > ")
                if self.V == 'back':
                    self.__init__()
                self.I = input("Enter current value > ")
                if self.I == 'back':
                    self.__init__()
                self.given_voltage_current()
        else:
            print("Invalid Entry!")
            self.__init__()

    def given_voltage_current(self):
        self.V = float(self.V)
        self.I = float(self.I)
        R = self.V/self.I
        print("Resistance R =", R)
        store = input("Store resistance instance? (y/n) ")
        if store == 'y':
            self.R.append(R)
            print("Instance stored as number ", len(self.R))
        return R

    def given_power_current(self):
        self.P = float(self.P)
        self.I = float(self.I)
        R = self.P**2/self.I
        print("Resistance R =", R)
        store = input("Store resistance instance? (y/n) ")
        if store == 'y':
            self.R.append(R)
            print("Instance stored as number ", len(self.R))
        return R

    def given_voltage_power(self):
        self.V = float(self.V)
        self.P = float(self.P)
        R = self.V**2/self.P
        print("Resistance R =", R)
        store = input("Store resistance instance? (y/n) ")
        if store == 'y':
            self.R.append(R)
            print("Instance stored as number ", len(self.R))
        return R

