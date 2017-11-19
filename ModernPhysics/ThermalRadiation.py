from PhotoelectricEffect import Essentials


class TRadiation(Essentials):

    #   Wien's displacement constant
    b = 2.8978e-3

    wave_length = []

    def blackbody_radiation(self):
        print("Blackbody radiation using Wien's displacement law")
        T = float(input("Temperature > "))
        w = self.b/T
        print("Black-body radiation wavelength w =", T)
        store = input("Store this wavelength instance? (y/n) ")
        if store == 'y':
            self.wave_length.append(w)
            print("Instance stored as number", len(self.wave_length))
        return w

