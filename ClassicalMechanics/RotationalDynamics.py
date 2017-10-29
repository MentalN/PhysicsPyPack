import math


class AngularVelocity:

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

    def ang_velocity_arc_length(self):
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
            print("Angular velocity instance stored as number:", len(AngularVelocity.omega))
        return w


def ang_velocity_menu():
    print("Given variable? ")
    print("[1] - Position")
    print("[2] - Tangential velocity")
    print("[3} - Frequency")
    print("[4} - Arc length")
    print("[5} - Acceleration")
    select = int(input("Enter choice number 1-5 > "))
    if select == 1:
        AngularVelocity.ang_velocity_position(AngularVelocity())
    elif select == 2:
        AngularVelocity.ang_velocity_tangential(AngularVelocity())
    elif select == 3:
        AngularVelocity.ang_velocity_frequency(AngularVelocity())
    elif select == 4:
        AngularVelocity.ang_velocity_arc_length(AngularVelocity())
    elif select == 5:
        print("Second variable? ")
        print("[1] - Time")
        print("[2] - Position")
        select2 = int(input("Enter choice (1/2) > "))
        if select2 == 1:
            AngularVelocity.ang_velocity_acceleration_time(AngularVelocity())
        elif select2 == 2:
            AngularVelocity.ang_velocity_acceleration_position(AngularVelocity())
        else:
            print("Invalid entry!")
    else:
        print("Invalid entry!")
    ang_velocity_menu()


ang_velocity_menu()

