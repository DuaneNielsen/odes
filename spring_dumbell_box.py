from vpython import *


ground = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, -1.5, 0))
top = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, 19.5, 0))
left = box(color=color.red, size=vector(1, 22, 1), pos=vector(-11, 9, 0))
right = box(color=color.red, size=vector(1, 22, 1), pos=vector(11, 9, 0))

L = 10  # m
m = 2  # kg
k = 4  # N/m
t = 0
dt = 0.001  # s

s1 = sphere(pos=vector(7, 2, 0))  # m
s2 = sphere(pos=vector(8, 5, 0))  # m

spring = helix(radius=0.5, thickness=0.3)

s1.oldpos = s1.pos - dt * vector(-4, 3, 0)
s2.oldpos = s2.pos - dt * vector(2, 7, 0)

g_ke_1 = gcurve(color=color.green)
g_ke_2 = gcurve(color=color.red)
g_pe_1 = gcurve(color=color.blue)
g_te = gcurve()


def collision(s):
    vx = s.r.x - s.oldpos.x
    vy = s.r.y - s.oldpos.y

    if s.r.x > 10.0:
        s.r.x, s.oldpos.x = 10.0, 10 + vx

    if s.r.x < -10.0:
        s.r.x, s.oldpos.x = -10.0, -10 + vx

    if s.r.y > 18.0:
        s.r.y, s.oldpos.y = 18.0, 18.0 + vy

    if s.r.y < 0.0:
        s.r.y, s.oldpos.y = 0.0, 0.0 + vy


while t < 60.0:
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
