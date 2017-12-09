from Thermodynamics.Essentials import Essentials
from math import sqrt

class IdealGas(Essentials):

    P_list = []
    V_list = []
    T_list = []
    n_list = []
    P = 0
    V = 0
    T = 0
    n = 0

    def select_variable(self):
        print("Choose a variable to solve for (case sensitive): ")
        print("Pressure (P)")
        print("Volume (V)")
        print("Number of moles (n)")
        print("Temperature (T)")
        var_input = input("> ")
        if var_input == 'P':
            self.V = input("Enter volume value > ")
            self.T = input("Enter temperature value > ")
            self.n = input("Enter number of moles > ")
            self.pressure()
        elif var_input == 'V':
            self.P = input("Enter pressure value > ")
            self.T = input("Enter temperature value > ")
            self.n = input("Enter number of moles > ")
            self.volume()
        elif var_input == 'n':
            self.P = input("Enter pressure value > ")
            self.V = input("Enter volume value > ")
            self.T = input("Enter temperature value > ")
            self.volume()
        elif var_input == 'T':
            self.P = input("Enter pressure value > ")
            self.V = input("Enter volume value > ")
            self.n = input("Enter number of moles > ")
            self.temperature()
        else:
            print("Invalid Entry!")
            self.select_variable()

    def pressure(self):
        self.V = float(self.V)
        self.T = float(self.T)
        self.n = float(self.n)
        P = self.n*self.R*self.T/self.V
        print("Pressure P =", P)
        store = input("Store this pressure instance? (y/n) ")
        if store == 'y':
            self.P_list.append(P)
            print("Instance stored as number ", len(self.P_list))
        return P

    def volume(self):
        self.P = float(self.P)
        self.T = float(self.T)
        self.n = float(self.n)
        V = self.n*self.R*self.T/self.P
        print("Volume V =", V)
        store = input("Store this volume instance? (y/n) ")
        if store == 'y':
            self.V_list.append(V)
            print("Instance stored as number ", len(self.V_list))
        return V

    def number_of_moles(self):
        self.P = float(self.P)
        self.V = float(self.V)
        self.T = float(self.T)
        n = self.P*self.V/self.R*self.T
        print("Number of moles n =", n)
        store = input("Store this moles instance? (y/n) ")
        if store == 'y':
            self.n_list.append(n)
            print("Instance stored as number ", len(self.n_list))
        return n

    def temperature(self):
        self.P = float(self.P)
        self.V = float(self.V)
        self.n = float(self.n)
        T = self.P*self.V/self.R*self.n
        print("Temperature T = ", T)
        store = input("Store this temperature instance? (y/n) ")
        if store == 'y':
            self.T_list.append(T)
            print("Instance stored as number ", len(self.T_list))
        return T


class Applications(Essentials):

    KE = []
    v_rms = []

    def average_KE(self):
        T = float(input("Enter temperature value > "))
        KE = 3/2*self.k_J*T
        print("Average molecular Kinetic energy KE =", KE)
        store = input("Store this energy instance? (y/n) ")
        if store == 'y':
            self.KE.append(KE)
            print("Instance stored as number ", KE)
        return KE

    def rms_velocity(self):
        M = float(input("Molar mass > "))
        T = float(input("Temperature > "))
        vrms = sqrt(3*self.R*T/M)
        print("RMS molecular velocity v =", vrms)
        store = input("Store this velocity instance? (y/n) ")
        if store == 'y':
            self.v_rms.append(vrms)
            print("Instance stored as number ", len(self.v_rms))
        return vrms



