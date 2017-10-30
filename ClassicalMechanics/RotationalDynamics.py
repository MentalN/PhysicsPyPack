import math


class Velocity:

    omega = []
    v_tan = []

    def ang_velocity_position(self):
        ti = float(input("Initial position angle > "))
        tf = float(input("Final position angle > "))
        dt = float(input("Change in time > "))
        w = (tf - ti)/dt
        print("Angular velocity w =", "%.2f" % w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            self.omega.append(w)
            print("Angular velocity instance stored as number:", len(self.omega))
        return w

    def ang_velocity_tangential(self):
        r = float(input("Radius > "))
        v = float(input("Tangential velocity > "))
        w = v/r
        print("Angular velocity w =",  "%.2f" %w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            self.omega.append(w)
            print("Angular velocity instance stored as number:", len(self.omega))
        return w

    def ang_velocity_frequency(self):
        f = float(input("Frequency of revolutions per second > "))
        w = 2 * math.pi * f
        print("Angular velocity w =",  "%.2f" %w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            self.omega.append(w)
            print("Angular velocity instance stored as number:", len(self.omega))
        return w

    def ang_velocity_arc_length(self):
        s  = float(input("Length of arc > "))
        r  = float(input("radius > "))
        dt = float(input("Change in time > "))
        w  = s/r*dt
        print("Angular velocity w =", "%.2f" % w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            self.omega.append(w)
            print("Angular velocity instance stored as number:", len(self.omega))
        return w

    def ang_velocity_acceleration_time(self):
        wi = float(input("Initial angular velocity > "))
        a  = float(input("angular acceleration > "))
        t  = float(input("Time > "))
        w  = wi + a*t
        print("Angular velocity w =", "%.2f" % w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            self.omega.append(w)
            print("Angular velocity instance stored as number:", len(self.omega))
        return w

    def ang_velocity_acceleration_position(self):
        wi = float(input("Initial angular velocity > "))
        a  = float(input("angular acceleration > "))
        dt = float(input("Change in position > "))
        w  = math.sqrt(wi*wi + 2 * a * dt)
        print("Angular velocity w =", "%.2f" % w, "rad/s")
        store = input("Store this angular velocity instance (y/n)? ")
        if store == 'y':
            self.omega.append(w)
            print("Angular velocity instance stored as number:", len(self.omega))
        return w

    def tangential_velocity(self):
        r = float(input("radius > "))
        w = input("Angular velocity, type 'stored' to use a stored instance > ")
        try:
            float(w)
        except ValueError:
            if w == "stored":
                num_w = int(input("Number of the stored instance > "))
                w = self.omega[num_w]
            else:
                print("Invalid entry!")
                self.tangential_velocity()
        v = r * w
        print("Tangential velocity v =", "%.2f" % v, "m/s")
        store = input("Store this tangential velocity instance (y/n)? ")
        if store == 'y':
            self.v_tan.append(v)
            print("tangential velocity instance stored as number:", len(self.v_tan))
        return v


class Forces:

    F_fugal = []
    F_petal = []

    def centrifugal_force(self):
        m = float(input("Mass of the object > "))
        r = float(input("Radius > "))
        w = input("Angular velocity, type 'stored' to use a stored instance > ")
        try:
            float(w)
        except ValueError:
            if w == "stored":
                num_w = int(input("Number of the stored instance > "))
                w = Velocity.omega[num_w]
            else:
                print("Invalid entry!")
                self.centrifugal_force()
        F = m * w * w * r
        print("Centrifugal Force F =", "%.2f" % F, "N")
        store = input("Store this Centrifugal Force instance (y/n)? ")
        if store == 'y':
            self.F_fugal.append(F)
            print("Centrifugal Force instance stored as number:", len(self.F_fugal))
        return F

    def centripetal_force(self):
        m = float(input("Mass of the object > "))
        r = float(input("Radius > "))
        v = input("Tangential velocity, type 'stored' to use a stored instance")
        try:
            float(v)
        except ValueError:
            if v == "stored":
                num_v = int(input("Number of the stored instance > "))
                v = Velocity.v_tan[num_v]
            else:
                print("Invalid entry!")
                self.centripetal_force()
        F = m * (v * v / r)
        print("Centripetal Force F =", "%.2f" % F, "N")
        store = input("Store this Centripetal Force instance (y/n)? ")
        if store == 'y':
            self.F_petal.append(F)
            print("Centripetal Force instance stored as number:", len(self.F_petal))
        return F


def ang_velocity_menu():
    print("Given variable? ")
    print("[1] - Position")
    print("[2] - Tangential velocity")
    print("[3} - Frequency")
    print("[4} - Arc length")
    print("[5} - Acceleration")
    select = int(input("Enter choice number 1-5 > "))
    if select == 1:
        Velocity.ang_velocity_position(Velocity())
    elif select == 2:
        Velocity.ang_velocity_tangential(Velocity())
    elif select == 3:
        Velocity.ang_velocity_frequency(Velocity())
    elif select == 4:
        Velocity.ang_velocity_arc_length(Velocity())
    elif select == 5:
        print("Second variable? ")
        print("[1] - Time")
        print("[2] - Position")
        select2 = int(input("Enter choice (1/2) > "))
        if select2 == 1:
            Velocity.ang_velocity_acceleration_time(Velocity())
        elif select2 == 2:
            Velocity.ang_velocity_acceleration_position(Velocity())
        else:
            print("Invalid entry!")
    else:
        print("Invalid entry!")
    ang_velocity_menu()


ang_velocity_menu()

