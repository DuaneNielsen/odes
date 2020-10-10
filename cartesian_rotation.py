from vpython import *

t = 0
dt = 1e-6
m = 1.0

s = sphere(size=vector(0.1, 0.1, 0.1))
s.r = 1.0
s.pos = vector(s.r, 0, 0)
s.velocity = vector(0, 0, 0)

attach_trail(s)

s.omega = 5 * pi

s.pos = vector(s.r * cos(s.omega * t), s.r * sin(s.omega * t), 0)
s.velocity = s.omega * s.r * vector(-sin(t * s.omega), cos(t * s.omega), 0)

while t < 13.0:
    s.accel = - s.r * (s.omega ** 2) * vector(cos(s.omega * t), sin(s.omega * t), 0)
    s.velocity += s.accel * dt
    s.pos += s.velocity * dt
    t += dt
    rate(1/dt)