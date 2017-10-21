import math


class AngularVelocity:

#   storing anguar velocity instances
    omega = []

    def ang_velocity_position(self):
        ti = float(input("Initial position angle > "))
        tf = float(input("Final position angle > "))
        dt = float(input("Change in time > "))
        w = (tf - ti)/dt
        print("Angular velocity w =", "%.2f" % w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            AngularVelocity.omega.append(w)
            print("Angular velocity instance stored as number:", len(AngularVelocity.omega))
        return w

    def ang_velocity_tangential(self):
        r = float(input("Radius > "))
        v = float(input("Tangential velocity > "))
        w = v/r
        print("Angular velocity w =",  "%.2f" %w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            AngularVelocity.omega.append(w)
            print("Angular velocity instance stored as number:", len(AngularVelocity.omega))
        return w

    def ang_velocity_frequency(self):
        f = float(input("Frequency of revolutions per second > "))
        w = 2 * math.pi * f
        print("Angular velocity w =",  "%.2f" %w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            AngularVelocity.omega.append(w)
            print("Angular velocity instance stored as number:", len(AngularVelocity.omega))
        return w

    def ang_velocity_arc_length(selfs):
        s  = float(input("Length of arc > "))
        r  = float(input("radius > "))
        dt = float(input("Change in time > "))
        w  = s/r*dt
        print("Angular velocity w =", "%.2f" % w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            AngularVelocity.omega.append(w)
            print("Angular velocity instance stored as number:", len(AngularVelocity.omega))
        return w

    def ang_velocity_acceleration_time(self):
        wi = float(input("Initial angular velocity > "))
        a  = float(input("angular acceleration > "))
        t  = float(input("Time > "))
        w  = wi + a*t
        print("Angular velocity w =", "%.2f" % w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            AngularVelocity.omega.append(w)
            print("Angular velocity instance stored as number:", len(AngularVelocity.omega))
        return w

    def ang_velocity_acceleration_position(self):
        wi = float(input("Initial angular velocity > "))
        a  = float(input("angular acceleration > "))
        dt = float(input("Change in position > "))
        w  = math.sqrt(wi*wi + 2 * a * dt)
        print("Angular velocity w =", "%.2f" % w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            AngularVelocity.omega.append(w)
            print("Angular velocity instance stored as number:", len(AngularVelocity.omega))
        return w




