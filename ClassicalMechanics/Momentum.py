import numpy
import math

class LinearMomentum:
    p = []

    def p_magnitude(self):
        print("Momentum magnitude")
        m = float(input("Mass of object > "))
        v = float(input("Velocity of object > "))
        p_mag = m * v
        print("Momentum magnitude P = ", "%.2f" % p_mag)
        store = input("Store this momentum instance (y/n)? ")
        if store == 'y':
            LinearMomentum.p.append(p_mag)
            print("Momentum instance stored as number:", len(LinearMomentum.p))

    def p_vector(self):
        print("Momentum vector")
        m  = float(input("Mass of the object > "))
        vx = float(input("Velocity x-component > "))
        vy = float(input("Velocity y-component > "))
        vz = float(input("Velocity z-component > "))
        v  = [vx, vy, vz]
        p_vec = m * numpy.array(v)
        print("Momentum vector P = ", p_vec)
        store = input("Store this momentum instance (y/n)? ")
        if store == 'y':
            LinearMomentum.p.append(p_vec)
            print("Momentum instance stored as number:", len(LinearMomentum.p))

    def collision_final_velocity(self):
        switch = input("Use stored momenta (y/n) ? ")
        if switch == 'y':
            p_num = int(input("Number of stored momentum to be used for p1_i > "))
            p1_i  = LinearMomentum.p[p_num]
            p_num = int(input("Number of stored momentum to be used for p2_i > "))
            p2_i  = LinearMomentum.p[p_num]
            p_num = int(input("Number of stored momentum to be used for p1_f > "))
            p1_f  = LinearMomentum.p[p_num]
            m2    = float(input("mass of the second object > "))
            vf_2  = (p1_i + p2_i - p1_f)/m2
            print("Velocity for second object after collision vf_2 =", "%.2f" % vf_2)
        m1 = float(input("Mass of the first object > "))
        vi_1 = float(input("Velocity of the first object > "))
        m2 = float(input("Mass of the second object > "))
        vi_2 = float(input("Velocity of the second object > "))
        vf_1 = float(input("Velocity of the first object after collision > "))
        vf_2 = (m1 * vi_1 + m2 * vi_2 - m1 * vf_1)/m2
        print("Velocity of the second object after collision vf2 = ", "%.2f" % vf_2)


class AngularMomentum(LinearMomentum):

    def L_magnitude(self):
        switch = input("Use stored momenta (y/n) ? ")
        if switch == 'y':
            p_num = int(input("Number of stored momentum to be used for p1_i > "))
            p     = LinearMomentum.p[p_num]
            r     = float(input("Direction magnitude > "))
            ang   = float(input("Degrees angle > "))
        m   = float(input("Mass > "))
        v   = float(input("Velocity magnitude > "))
        r   = float(input("Direction magnitude > "))
        ang = float(input("Degrees angle > "))
        L_mag = m*v*r*math.sin(math.radians(ang))
        print("Angular Momentum magnitude L = ", "%.2f" % L_mag)
        store = input("Store this momentum instance (y/n)? ")
        if store == 'y':
            LinearMomentum.p.append(L_mag)
            print("Momentum instance stored as number:", len(LinearMomentum.p))

    def L_vector(self):
        switch = input("Use stored momenta (y/n) ? ")
        if switch == 'y':
            p_num = int(input("Number of stored momentum vector to be used for P > "))
            p     = LinearMomentum.p[p_num]
        else:
            m  = float(input("Mass of the object >"))
            vx = float(input("Velocity x-component > "))
            vy = float(input("Velocity y-component > "))
            vz = float(input("Velocity z-component > "))
            v = [vx, vy, vz]
            p = m * numpy.array(v)
        print("Direction vector > ")
        rx = float(input("Direction x-component > "))
        ry = float(input("Direction y-component > "))
        rz = float(input("Direction z-component > "))
        r  = [rx, ry, rz]
        L_vec = numpy.cross(r, p)
        print("Angular Momentum vector L = ", "%.2f" % L_vec)
        store = input("Store this momentum instance (y/n)? ")
        if store == 'y':
            LinearMomentum.p.append(L_vec)
            print("Momentum instance stored as number:", len(LinearMomentum.p))


def menu():
    print("[1] - Momentum magnitude")
    print("[2] - Momentum vector")
    print("[3] - Linear momentum final velocity")
    print("[4] - Angular momentum magnitude")
    print("[5] - Angular momentum vector")
    select = int(input("Select a computation > "))
    if select == 1:
        LinearMomentum.p_magnitude(LinearMomentum())
    elif select == 2:
        LinearMomentum.p_vector(LinearMomentum())
    elif select == 3:
        LinearMomentum.collision_final_velocity(LinearMomentum())
    elif select == 4:
        AngularMomentum.L_magnitude(AngularMomentum())
    elif select == 5:
        AngularMomentum.L_vector(AngularMomentum())
    menu()


menu()
