from vpython import *

dt = 1e-5
t = 0

s1 = sphere(color=color.red)
s2 = sphere(color=color.blue)

s1.mass = 2
s1.pos = vector(-5, 0, 0)
s1.velocity = vector(5, 0, 0)

s2.mass = 1
s2.pos = vector(5, 0.2, 0)
s2.velocity = vector(-3, 0, 0)

p1 = gcurve(color=color.red)
p2 = gcurve(color=color.blue)
pt = gcurve()

k = 10.0  # N/m^12

while t < 10.0:
    s1.force = k * (s1.pos - s2.pos) / (s1.pos - s2.pos).mag ** 3
    s2.force = - s1.force

    s1.velocity += s1.force/s1.mass * dt
    s1.pos += s1.velocity * dt

    s2.velocity += s2.force/s2.mass * dt
    s2.pos += s2.velocity * dt

    p1.plot(pos=(t, s1.velocity.mag * s1.mass))
    p2.plot(pos=(t, s2.velocity.mag * s2.mass))
    pt.plot(pos=(t, s1.velocity.mag * s1.mass + s2.velocity.mag * s2.mass))

    t += dt
    rate(1/dt)