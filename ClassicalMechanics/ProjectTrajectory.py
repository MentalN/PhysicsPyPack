import math


class Projectile:

    gravity = 9.81

    def TrajectoryNoFloor(self, time, vo, azimuth, elevation, xo, yo, zo):
        print('Time (s)        x-location (m)        y-location        z-location')
        for t in range(time+1):
            x = vo * math.cos(math.radians(azimuth)) * math.cos(math.radians(elevation)) * t + xo
            y = vo * math.sin(math.radians(azimuth)) * math.cos(math.radians(elevation)) * t + yo
            z = vo * math.sin(math.radians(elevation)) * t - 0.5 * Projectile.gravity * t * t + zo
            print(t, end='')
            print("               %.2f" %x, end='')
            print("                  %.2f" %y, end='')
            print("                %.2f" %z)
        print("_________________________________________________________")

    def TrajectoryFloor(self, time, vo, azimuth, elevation, xo, yo, zo):
        print('Time (s)        x-location (m)        y-location        z-location')
        for t in range(time+1):
            x = vo * math.cos(math.radians(azimuth)) * math.cos(math.radians(elevation)) * t + xo
            y = vo * math.sin(math.radians(azimuth)) * math.cos(math.radians(elevation)) * t + yo
            z = vo * math.sin(math.radians(elevation)) * t - 0.5 * Projectile.gravity * t * t + zo
            print(t, end='')
            print("               %.2f" %x, end='')
            print("                  %.2f" %y, end='')
            print("                %.2f" %z)
            if z < 0:
                break
        print("________________________Floor_______________________________")


n_projectile = int(input('Number of projectiles > '))
projectile_list= [Projectile for i in range(n_projectile)]
ti = int(input('Time interval > '))
g = input('Enable earth gravity? (y/n) > ')
if g=='n':
    Projectile.gravity = 0
floor_switch = input('Put floor? (y/n) > ')


for j in range(n_projectile):
    print('// Parameters for object number [', j+1, '] // ')
    vi = float(input('Initial Velocity >'))
    az = float(input('Azimuth degrees > '))
    el = float(input('Elevation degrees > '))
    xi = float(input('launch x-coordinates > '))
    yi = float(input('launch y-coordinates > '))
    zi = float(input('launch z-coordinates > '))
    if floor_switch == 'n':
        projectile_list[j].TrajectoryNoFloor(projectile_list[j], ti, vi, az, el, xi, yi, zi)
    else:
        projectile_list[j].TrajectoryFloor(projectile_list[j], ti, vi, az, el, xi, yi, zi)




