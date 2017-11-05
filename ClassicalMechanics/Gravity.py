class Gravity:

    G  = 6.67408*10**-11
    Me = 5.972*10**24
    Re = 6.371*10**6

    F_g = []
    U_g = []

    def gravitational_force(self, r, m):
        F = (self.G*self.Me*m)/((r+self.Re)**2)
        print('Gravitational Force = ', "%.2f" % F, 'N')
        store = input("Store this gravitational force instance? (y/n)")
        if store == 'y':
            self.F_g.append(F)
            print("Instance stored as number [", len(self.F_g), "]")
        return F

    def gravitational_potential(self, r, m):
        U = (self.G*self.Me*m)/(r+self.Re)
        print('Gravitational Potential Energy = ', "%.2f" % U, 'J')
        store = input("Store this gravitational potential instance? (y/n)")
        if store == 'y':
            self.U_g.append(U)
            print("Instance stored as number [", len(self.U_g), "]")
        return U

    def gravity_menu(self):
        print('[1] - Gravitational Force')
        print('[2] - Gravitational Potential Energy')
        select = int(input('Select an option > '))

        distance = float(input('Distance from earth surface > '))
        mass = float(input('Mass of the object > '))

        if select == 1:
            self.gravitational_force(distance, mass)
        elif select == 2:
            self.gravitational_potential(distance, mass)
        else:
            print("invalid Entry!")
