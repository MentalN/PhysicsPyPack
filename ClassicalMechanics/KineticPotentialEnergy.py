import math
from KinematicEquations import Velocity, Distance
from prettytable import PrettyTable


class KineticPotentialEnergy:

    def ConversionTable(self):
        m  = float(input("Object's mass > "))
        hi = float(input("Object's initial height > "))
        table = PrettyTable(['Time (s)', 'Height(m)', 'Potential Energy(J)', 'Velocity(m/s)', 'Kinetic Energy(J)'])
        for t in range(0, 15):
            h  = hi - Distance.DistanceFinal2Return(Distance(), 0, 0, t, 9.81)
            if h <= 0:
                tf = math.sqrt(2*hi/9.81)
                hf = hi - Distance.DistanceFinal2Return(Distance(), 0, 0, tf, 9.81)
                pe = m * 9.81 * hf
                vf  = Velocity.VelocityFinal1Return(Velocity(), 0, 9.81, tf)
                ke = 0.5 * m * vf * vf
                table.add_row(["%.2f" % tf, "%.2f" % hf, "%.2f" % pe, "%.2f" % vf, "%.2f" % ke])
                break
            pe = m * 9.81 * h
            v  = Velocity.VelocityFinal1Return(Velocity(), 0, 9.81, t)
            ke = 0.5 * m * v * v
            table.add_row(["%.2f" % t, "%.2f" % h, "%.2f" % pe, "%.2f" % v, "%.2f" % ke])
        print(table)


KineticPotentialEnergy.ConversionTable(KineticPotentialEnergy())
