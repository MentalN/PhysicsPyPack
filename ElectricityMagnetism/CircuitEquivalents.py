class Resistance:

    R = []

    def parallel_resistors(self):
        num_R = int(input("Number of resistors in parallel > "))
        R_eq = 0
        for x in range(num_R):
            print("Enter the resistance value of Resistor [", x+1, "]")
            R_n = float(input("> "))
            R_eq += 1/R_n
        R_eq = R_eq ** -1
        print("Equivalent resistance R =", "%.2f" % R_eq)
        store = input("Store this resistance instance? (y/n) ")
        if store == 'y':
            self.R.append(R_eq)
            print("Resistance instance stored as number [", len(self.R), "]")

    def series_resistors(self):
        num_R = int(input("Number of resistors in series > "))
        R_eq = 0
        for x in range(num_R):
            print("Enter the resistance value of Resistor [", x+1, "]")
            R_n = float(input("> "))
            R_eq += R_n
        print("Equivalent resistance R =", "%.2f" % R_eq)
        store = input("Store this resistance instance? (y/n) ")
        if store == 'y':
            self.R.append(R_eq)
            print("Resistance instance stored as number [", len(self.R), "]")


class Capacitance:

    C = []

    def parallel_capacitors(self):
        num_C = int(input("Number of capacitors in parallel > "))
        C_eq = 0
        for x in range(num_C):
            print("Enter the capacitor value of Capacitor [", x + 1, "]")
            C_n = float(input("> "))
            C_eq += C_n
        print("Equivalent capacitance C =", "%.2f" % C_eq)
        store = input("Store this capacitance instance? (y/n) ")
        if store == 'y':
            self.C.append(C_eq)
            print("Capacitance instance stored as number [", len(self.C), "]")

    def series_capacitors(self):
        num_C = int(input("Number of capacitors in series > "))
        C_eq = 0
        for x in range(num_C):
            print("Enter the capacitor value of Capacitor [", x + 1, "]")
            C_n = float(input("> "))
            C_eq += 1/C_n
        C_eq = C_eq ** -1
        print("Equivalent capacitance C =", "%.2f" % C_eq)
        store = input("Store this capacitance instance? (y/n) ")
        if store == 'y':
            self.C.append(C_eq)
            print("Capacitance instance stored as number [", len(self.C), "]")


class Inductance:

    L = []

    def parallel_inductors(self):
        num_L = int(input("Number of inductors in parallel > "))
        L_eq = 0
        for x in range(num_L):
            print("Enter the inductance value of Inductor [", x+1, "]")
            L_n = float(input("> "))
            L_eq += 1/L_n
        L_eq = L_eq ** -1
        print("Equivalent inductance L =", "%.2f" % L_eq)
        store = input("Store this inductance instance? (y/n) ")
        if store == 'y':
            self.L.append(L_eq)
            print("inductance instance stored as number [", len(self.L), "]")

    def series_inductors(self):
        num_L = int(input("Number of inductors in series > "))
        L_eq = 0
        for x in range(num_L):
            print("Enter the inductance value of Inductor [", x+1, "]")
            L_n = float(input("> "))
            L_eq += L_n
        print("Equivalent inductance L =", "%.2f" % L_eq)
        store = input("Store this inductance instance? (y/n) ")
        if store == 'y':
            self.L.append(L_eq)
            print("inductance instance stored as number [", len(self.L), "]")
