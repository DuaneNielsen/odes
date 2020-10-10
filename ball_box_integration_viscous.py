from vpython import *

ground = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, -1.5, 0))
top = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, 19.5, 0))
left = box(color=color.red, size=vector(1, 22, 1), pos=vector(-11, 9, 0))
right = box(color=color.red, size=vector(1, 22, 1), pos=vector(11, 9, 0))


s = sphere()
s.pos = vector(-10, 0, 0)
s.velocity = vector(5, 19.2, 0)

gravity = vector(0, -9.8, 0)
t = 0
dt = 0.01
viscuosity = 0.2

while t < 20:
    s.velocity += (gravity - viscuosity * s.velocity) * dt
    s.pos += s.velocity * dt
    t = t + dt
    rate(abs(1.0 / dt))
    if not -10.0 < s.pos.x < 10.0:
        s.velocity.x = - s.velocity.x
    if not 0.0 < s.pos.y < 19.0:
        s.velocity.y = - s.velocity.y
