import math


class Distance:

    def Switch(self):
        switch = input('velocity constant? (y/n) ')
        if switch == 'y':
            Distance.DistanceFinal1(self)
        elif switch == 'n':
            Distance.DistanceFinal2(self)
        else:
            print('invalid input!')
            Distance.Switch()
    def DistanceFinal1(self):
        distance_i = float(input('Initial distance > '))
        velocity_i = float(input('Initial Velocity > '))
        time       = float(input('Change in Time   > '))
        distance_f = distance_i + velocity_i*time
        print('Final distance = ', distance_f)
    def DistanceFinal2(self):
        distance_i    = float(input('Initial distance > '))
        velocity_i    = float(input('Initial Velocity > '))
        time          = float(input('Change in Time   > '))
        acceleration  = float(input('Acceleration     > '))
        distance_f    = distance_i + velocity_i*time + 0.5*acceleration*time*time
        print('Final distance = ', distance_f)


class Velocity:

    def Switch(self):
        switch = input('Changee in time known? (y/n) ')
        if switch == 'y':
            Velocity.VelocityFinal1(self)
        elif switch == 'n':
            Velocity.VelocityFinal2(self)
        else:
            print('invalid input!')
            Velocity.Switch()
    def VelocityFinal1(self):
        velocity_i   = float(input('Initial Velocity > '))
        acceleration = float(input('Acceleration     > '))
        time         = float(input('Change in Time   > '))
        velocity_f   = velocity_i + acceleration*time
        print('Final velocity = ', velocity_f)
    def VelocityFinal2(self):
        displacement = float(input('Displacement > '))
        velocity_i   = float(input('Initial Velocity > '))
        acceleration = float(input('acceleration     > '))
        velocity_f   = math.sqrt((velocity_i*velocity_i + 2*acceleration*displacement))
        print('Final velocity = ', velocity_f)


def menu():
    print('[1] Find final distance')
    print('[2] Find final velocity')
    index_a = input('select a value > ')
    if index_a == '1':
        outputA = Distance()
    elif index_a == '2':
        outputA = Velocity()
    else:
        print('Invaid input!')
        menu()
    outputA.Switch()
    print('__________________\n')
    menu()

menu()
