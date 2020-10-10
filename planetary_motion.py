from vpython import *
from copy import copy

t = 0.0
dt = 60.0 * 60.0

m_e = 5.97e24  # kg
m_s = 1.99e30  # kg
moon_earth_d = 362600e3
G = 6.67300e-11  # Nm^2/kg^2
au = 149.6e9  # m
year = 31556926  # s


class Celestial(sphere):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.m = kwargs['m']
        self.r = kwargs['r']
        self.pos = kwargs['r']
        self.prev = kwargs['r']

    @property
    def velocity(self):
        return (self.r - self.prev) / dt

    def update(self, f):
        self.r, self.prev = 2 * self.r - self.prev + (f * dt ** 2) / self.m, self.r
        self.pos = self.r


def orb_v(m, r):
    return sqrt(G * m / r)


sun = Celestial(r=vector(0, 0, 0), m=1.99e30, radius=6.957e8, color=color.yellow)
earth = Celestial(r=vector(au, 0, 0), m=5.97e24, radius=6378e3, color=color.blue, make_trail=True)
moon = Celestial(r=vector(au + moon_earth_d, 0, 0), m=7.342e22, radius=1736e3)

sun.v0 = vector(0, - sqrt(G * m_e / au), 0)
sun.prev = sun.r - sun.v0 * dt

earth.v0 = vector(0, orb_v(sun.m, au) - orb_v(moon.m, moon_earth_d), 0)
earth.v0 = vector(0, orb_v(sun.m, au), 0)
earth.prev = earth.r - earth.v0 * dt

moon.v0 = vector(0, orb_v(sun.m, au) + orb_v(earth.m, moon_earth_d), 0)
moon.prev = moon.r - moon.v0 * dt


def kinetic(s, m):
    return 0.5 * m * s.velocity.mag ** 2


def pe_grav(s1, s2):
    return -G * s1.m * s2.m / (s1.r - s2.r).mag


def g_force(s1, s2):
    r = s1.r - s2.r
    return G * s1.m * s2.m * r / r.mag ** 3


c_kin_e = gcurve(color=color.red)
c_grav_e = gcurve(color=color.blue)
c_tot_e = gcurve()

while t <= 600 * year:
    f = g_force(sun, earth)
    f_e = g_force(earth, moon)
    f_s = g_force(sun, moon)
    #f_e, f_s = vector(0, 0, 0), vector(0, 0, 0)

    sun.update(-f - f_s)
    moon.update(f_e + f_s)
    earth.update(f - f_e)

    p_grav = pe_grav(sun, earth)
    k = kinetic(earth, m_e) + kinetic(sun, m_s)
    c_kin_e.plot((t, k))
    c_grav_e.plot((t, p_grav))
    c_tot_e.plot((t, k + p_grav))

    scene.center = earth.r
    t += dt
    rate(12 * 24)