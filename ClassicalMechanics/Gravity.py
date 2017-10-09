class Gravity:
    G  = 6.67408*10**-11
    Me = 5.972*10**24
    Re = 6.371*10**6

    def GraviationalForce(self, r, m):
        F = (Gravity.G*Gravity.Me*m)/((r+Gravity.Re)**2)
        print('Gravitational Force = ', "%.2f" %F, 'N')

    def GravitationalPotential(self, r, m):
        U = (Gravity.G*Gravity.Me*m)/(r+Gravity.Re)
        print('Gravitational Potential Energy = ', "%.2f" %U, 'J')


print('[1] - Graviational Force')
print('[2] - Gravitational Potential Energy')
select = int(input('Select an option > '))

distance = float(input('Distance from earth surface > '))
mass     = float(input('Mass of the object > '))

if select == 1:
    Gravity.GraviationalForce(Gravity(), distance, mass)
elif select == 2:
    Gravity.GravitationalPotential(Gravity(), distance, mass)