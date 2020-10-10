from vpython import *

L = 10  # m
m = 2  # kg
k = 4  # N/m
g = vector(0, -9.8, 0)  # m/s2
t = 0
dt = 0.001  # s

pin = vector(0, 0, 0)
s1 = sphere(pos=vector(8, -3, 0), color=color.green)  # m
s2 = sphere(pos=vector(-2, 4, 0))  # m)

spring1 = helix(radius=0.5, thickness=0.3)
spring2 = helix(radius=0.5, thickness=0.3)

s1.oldpos = s1.pos - dt * vector(-3, -2, 1)
s2.oldpos = s2.pos - dt * vector(3, 2, 1)

g_ke_1 = gcurve(color=color.green)
g_ke_2 = gcurve(color=color.red)
g_pe_1 = gcurve(color=color.blue)
g_pe_2 = gcurve(color=color.blue)
g_te = gcurve()


def springforce(k, pos1, pos2):
    svec = pos1 - pos2
    return -k * (svec.mag - L) * (svec / svec.mag)


while t < 180.0:

    s1.force = springforce(k, s1.pos, s2.pos) + springforce(k, s1.pos, pin) + m * g
    s2.force = springforce(k, s2.pos, s1.pos) + m * g

    s1.pos, s1.oldpos =\
        2*s1.pos - s1.oldpos + s1.force * dt ** 2 / m, 1 * s1.pos
    s2.pos, s2.oldpos =\
        2*s2.pos - s2.oldpos + s2.force * dt ** 2 / m, 1 * s2.pos
    spring1.pos, spring1.axis = s2.pos, s1.pos - s2.pos
    spring2.pos, spring2.axis = pin, s1.pos

    ke_1 = 0.5 * m * ((s1.pos - s1.oldpos).mag/dt) ** 2
    ke_2 = 0.5 * m * ((s2.pos - s2.oldpos).mag/dt) ** 2
    pe_1 = 0.5 * k * ((s1.pos - s2.pos).mag - L) ** 2
    pe_2 = 0.5 * k * ((pin - s1.pos).mag - L) ** 2
    ge_1 = - s1.pos.y * g.y * m - s2.pos.y * g.y * m

    te = ke_1 + ke_2 + pe_1 + pe_2 + ge_1

    g_ke_1.plot((t, ke_1))
    g_ke_2.plot((t, ke_2))
    g_pe_1.plot((t, pe_1))
    g_pe_2.plot((t, pe_2))
    g_te.plot((t, te))

    t += dt
    rate(2.0/dt)
