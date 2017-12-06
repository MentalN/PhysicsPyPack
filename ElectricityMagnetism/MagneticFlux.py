from ElectricityMagnetism.MagneticField import Field
from math import cos, radians


class Flux(Field):

    b_flux = []

    def magnetic_field(self):
        B = float(input("Magnetic Field > "))
        A = float(input("Area > "))
        theta = radians(float(input("Angle > ")))
        phi = B * A * cos(theta)
        print("Electric Flux = ", phi)
        store = input("Store this flux instance? (y/n) ")
        if store == 'y':
            self.b_flux.append(phi)
            print("Instance stored as number ", len(self.b_flux))
        return phi

