from vpython import *

L = 10  # m
m = 2  # kg
k = 4  # N/m
t = 0
dt = 0.001  # s

s1 = sphere(pos=vector(8, -3, 0))  # m
s2 = sphere(pos=vector(0, 0, 0))  # m

spring = helix(radius=0.5, thickness=0.3)

s1.oldpos = s1.pos - dt * vector(-3, -2, 1)
s2.oldpos = s2.pos - dt * vector(3, 2, 1)

g_ke_1 = gcurve(color=color.green)
g_ke_2 = gcurve(color=color.red)
g_pe_1 = gcurve(color=color.blue)
g_te = gcurve()


def collision(s):
    if not -10.0 < s.r.x < 10.0:
        s.velocity.x = - s.velocity.x
    if not 0.0 < s.r.y < 19.0:
        s.velocity.y = - s.velocity.y


while t < 6.0:
    svec = s1.pos - s2.pos
    s1.force = -k * (svec.mag - L) * (svec / svec.mag)
    s2.force = -s1.force

    s1.pos, s1.oldpos =\
        2*s1.pos - s1.oldpos + s1.force * dt ** 2 / m, 1 * s1.pos
    s2.pos, s2.oldpos =\
        2*s2.pos - s2.oldpos + s2.force * dt ** 2 / m, 1 * s2.pos
    spring.pos, spring.axis = s2.pos, s1.pos - s2.pos

    ke_1 = 0.5 * m * ((s1.pos - s1.oldpos).mag/dt) ** 2
    ke_2 = 0.5 * m * ((s2.pos - s2.oldpos).mag/dt) ** 2
    pe_1 = 0.5 * k * ((s1.pos - s2.pos).mag - L) ** 2
    te = ke_1 + ke_2 + pe_1

    g_ke_1.plot((t, ke_1))
    g_ke_2.plot((t, ke_2))
    g_pe_1.plot((t, pe_1))
    g_te.plot((t, te))

    collision(s1)
    collision(s2)

    t += dt
    rate(1/dt)
