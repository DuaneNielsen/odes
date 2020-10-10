from vpython import *

ground = box(color=color.red)
ground.size = vector(22, 1, 2)  # meters
ground.pos = vector(0, -1.5, 0)  # meters

s = sphere()
t = 0  # seconds
dt = 0.01  # seconds
v = 10  # meters/second
while t < 1:  # second
    s.pos = vector(v * t, 0, 0)  # meters
    t = t + dt
    rate(1 / dt)
