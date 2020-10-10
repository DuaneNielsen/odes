from vpython import *

s = sphere()
t = 0  # seconds
dt = 0.001  # seconds
R = 10  # meters
omega = 2  # radians/second
while t < 6 * pi / omega:
    s.pos = vector(R * sin(omega * t), R * cos(omega * t / 2), 0)
    t = t + dt
    rate(1 / dt)
