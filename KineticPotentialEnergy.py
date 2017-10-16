import math
from KinematicEquations import Velocity, Distance
from prettytable import PrettyTable


class KineticPotentialEnergy:

    def OutputTable(self):
        table = PrettyTable(['Time (s)', 'Height(m)', 'Potential Energy(J)', 'Velocity(m/s)', 'Kinetic Energy(J)'])
        m = float(input('Mass of the object (kg) > '))
        hi = float(input('Distance of the object from the ground in meters > '))
        #final values for when the object finally hit the ground - START
        tf = math.sqrt(2*hi/9.81)
        hf = Distance.DistanceFinal2Return(Distance(), 0, 0, tf, 9.81)
        dh = hi - hf
        PE_f = m * 9.81 * dh
        vf = Velocity.VelocityFinal1Return(Velocity(), 0, 9.81, tf)
        KE_f = 0.5 * m * vf * vf
        # ~~~~~~END
        for t in range(0, 9):
            height = hi - Distance.DistanceFinal2Return(Distance(), 0, 0, t, 9.81)
            if height <= 0:
                table.add_row(["%.2f" %tf, "%.2f" %dh, "%.2f" %PE_f, "%.2f" %vf, "%.2f" %KE_f])
                break
            PE = mass * 9.81* height
            v = Velocity.VelocityFinal1Return(Velocity(), 0, 9.81, t)
            KE = 0.5 * mass * v * v
            table.add_row([t, "%.2f" %height, "%.2f" %PE, "%.2f" %v, "%.2f" %KE])
        print(table)


KineticPotentialEnergy.OutputTable(KineticPotentialEnergy())
