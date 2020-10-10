from vpython import *

G = 6.67300e-11

s1 = sphere(color=color.blue)
s1.m = 1e10
s1.pos = vector(1e1, 0, 0)
s1.accel = vector(0, 0, 0)
s1.velocity = vector(0, 0, 0)

s2 = sphere(color=color.red)
s2.m = 1e10
s2.pos = vector(0, 0, 0)
s2.accel = vector(0, 0, 0)
s2.velocity = vector(0, 0, 0)

t = 0
dt = 0.1


def gravity(s1, s2):
    r = s1.r - s2.r
    f = - G * s1.m * s2.m * r / r.mag ** 3
    return f


def update(s, f):
    s.accel = f / s.m
    s.velocity += s.accel * dt
    s.r += s.velocity * dt


def kinetic(s):
    return 0.5 * s.m * s.velocity.mag ** 2


def grav_potential(s1, s2):
    return - G * s1.m * s2.m / (s1.r - s2.r).mag


g1 = graph()
g2 = graph()
kinetic_s1_g = gcurve(graph=g1, color=color.red)
kinetic_s2_g = gcurve(color=color.green)
grav_g = gcurve(graph=g2, color=color.blue)
total = gcurve()

while t < 6:
    f = gravity(s1, s2)
    update(s1, f)

    # f = gravity(s2, s1)
    # update(s2, f)

    kinetic_s1_g.plot((t, kinetic(s1)))
    grav_g.plot((t, -G * s1.m * s2.m / s1.pos.mag))
    tot = kinetic(s1) + -G * s1.m * s2.m / s1.pos.mag
    total.plot((t, tot))

    t += dt
    rate(10)

