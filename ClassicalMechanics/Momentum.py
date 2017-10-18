import numpy


class LinearMomentum:
    num_p = 0
#   Actual number of momentum instances is "num_p - 1" when calling them form the list p
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
            LinearMomentum.num_p += 1
            print("Momentum instance stored as number:", (LinearMomentum.num_p))

    def p_vector(self):
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
            LinearMomentum.num_p += 1
            print("Momentum instance stored as number:", (LinearMomentum.num_p))

    def collision_final_velocity(self):
        switch = input("Use stored momenta (y/n) ? ")


LinearMomentum.p_magnitude(LinearMomentum())
