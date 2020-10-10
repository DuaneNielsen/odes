from vpython import *

s = sphere()
t = 0  # seconds
dt = 0.001  # seconds
s.R = 10  # meters
g = - 9.8
s.omega = 0.8  # radians/second
s.theta = - pi  # radians


while t < 6 * pi:

    s.angular_accel = - g/s.R * sin(s.theta)
    s.omega += s.angular_accel * dt
    s.theta += s.omega * dt

    s.pos = vector(s.R * sin(s.theta), s.R * cos(s.theta), 0)
    t = t + dt
    rate(1 / dt)
