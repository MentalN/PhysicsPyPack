import math


class Projectile:

    def TrajectoryNoFloor(self, time, vo, azimuth, elevation, xo, yo, zo):
        print('Time (s)        x-location (m)        y-location        z-location')
        for t in range(time+1):
            x = vo * math.cos(math.radians(azimuth)) * math.cos(math.radians(elevation)) * t + xo
            y = vo * math.sin(math.radians(azimuth)) * math.cos(math.radians(elevation)) * t + yo
            z = vo * math.sin(math.radians(elevation)) * t - 0.5 * 9.81 * t * t + zo
            print(t, end='')
            print("               %.2f" %x, end='')
            print("                  %.2f" %y, end='')
            print("                %.2f" %z)

    def TrajectoryFloor(self, time, vo, azimuth, elevation, xo, yo, zo):
        print('Time (s)        x-location (m)        y-location        z-location')
        for t in range(time):
            x = vo * math.cos(math.radians(azimuth)) * math.cos(math.radians(elevation)) * t + xo
            y = vo * math.sin(math.radians(azimuth)) * math.cos(math.radians(elevation)) * t + yo
            z = vo * math.sin(math.radians(elevation)) * t - 0.5 * 9.81 * t * t + zo
            if z <= 0:
                xf = x
                yf = y
                zf = z


n_projectile = int(input('Number of projectiles > '))
projectile_list= [Projectile for i in range(n_projectile)]
ti = int(input('Time interval > '))

for j in range(n_projectile):
    print('// Parameters for object number [', j+1, '] // ')
    vi = float(input('Initial Velocity >'))
    az = float(input('Azimuth degrees > '))
    el = float(input('Elevation degrees > '))
    xi = float(input('launch x-coordinates > '))
    yi = float(input('launch y-coordinates > '))
    zi = float(input('launch z-coordinates > '))
    projectile_list[j].TrajectoryNoFloor(projectile_list[j], ti, vi, az, el, xi, yi, zi)


