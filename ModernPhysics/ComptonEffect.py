from ModernPhysics.Essentials import Essentials
import math


class Compton(Essentials):

    compton_dl = []
    compton_angle = []

    def wavelength_change(self):
        theta = float(input("Scattering angle in degrees > "))
        theta = math.radians(theta)
        a = self.h/(self.particles["electron"]*self.c)
        b = (1-math.cos(theta))
        dl = a * b
        print("Change in wavelength =", dl)
        store = input("Store this wavelength instance? (y/n) ")
        if store == 'y':
            self.compton_dl.append(dl)
            print("Instance stored as number", len(self.compton_dl))
        return dl

    def scattering_angle(self):
        dl = input("Change in wavelength, type 'store' to use a stored instance> ")
        try:
            float(dl)
        except ValueError:
            if dl == "store":
                num = int(input("Instance number > "))
                dl = self.compton_dl[num - 1]
            else:
                print("Invalid entry!")
                self.scattering_angle()
        a = dl*self.particles["electron"]*self.c/self.h
        theta = math.degrees(math.acos(1-a))
        print("Scattering angle = ", theta, "Degree")
        store = input("Store this angle instance? (y/n) ")
        if store == 'y':
            self.compton_angle.append(theta)
            print("Instance stored as number", len(self.compton_angle))
        return theta
    
#    def scattered_direction(self):
#    P89 Example 3.7 part d
