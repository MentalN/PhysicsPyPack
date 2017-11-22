from ClassicalMechanics.Momentum import LinearMomentum
from ModernPhysics.Essentials import Essentials


class Heisenberg(LinearMomentum, Essentials):

    dx_list = []
    dp_list = []

    def position_uncertainty(self):
        dp = input("Momentum. Or to calculate it, type 'calc' > ")
        try:
            float(dp)
        except ValueError:
            if dp == "calc":
                dp = self.p_magnitude()
            else:
                print("Invalid entry!")
                self.position_uncertainty()
        dx = self.h_bar/dp
        print("Uncertainty in position = ", dx)
        store = input("Store this uncertainty instance? (y/n) ")
        if store == 'y':
            self.dx_list.append(dx)
            print("Instance stored as number ", len(self.dx_list))
        return dx

    def momentum_uncertainty(self):
        dx = input("Region width, or type 'stored' to use a stored instance")
        try:
            float(dx)
        except ValueError:
            if dx == "stored":
                num_dx = int(input("Number of stored instance >"))
                dx = self.dx_list[num_dx]
            else:
                print("Invalid entry!")
                self.momentum_uncertainty()
        dp = self.h_bar/dx
        print("Uncertainty in momentum = ", dp)
        store = input("Store this uncertainty instance? (y/n) ")
        if store == 'y':
            self.dp_list.append(dp)
            print("Instance stored as number ", len(self.dp_list))
        return dp
