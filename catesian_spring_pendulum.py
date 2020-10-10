from vpython import *

t = 0
dt = 1e-3

k = 0.5
g = vector(0, -9.8, 0)
eps = 1e-8
m = 0.3

c = sphere(color=color.green)
c.pos = vector(0, 0, 0)

s = sphere()
s.pos = vector(-2, 0, 0)
s.velocity = vector(0.0, 0, 0)
s.accel = vector(0, 0, 0)
s.spring_force = k * - s.pos
attach_arrow(s, "spring_force", shaftwidth=0.3)
gravity_arrow = arrow(color=color.blue)

while t < 100:
    s.spring_force = k * - s.pos - vector(0, 10, 0)

    gravity_arrow.pos = s.pos
    gravity_arrow.axis = g * m

    s.accel = g + (s.spring_force / m)
    s.velocity += s.accel * dt
    s.pos += s.velocity * dt

    t += dt
    rate(1/dt)