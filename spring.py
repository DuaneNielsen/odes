from vpython import sphere, helix, box, cylinder, cone, color, gcurve, rate
from vpython import sqrt, atan, cos, sin, pi, dot
from vpython import vector
from copy import copy

kinetic = gcurve(color=color.blue)
potential = gcurve(color=color.red)
energy = gcurve(color=color.black)
thermal = gcurve(color=color.green)

m = 2  # kg
k = 4  # N/m
d = 2

t = 0
dt = 0.01  # s

s = sphere()
spring = helix(radius=0.6, thickness=0.3)

s.velocity = vector(-10, 0, 0)
s.pos = vector(10, 0, 0) * dt  # m
s.prev_pos = s.pos - s.velocity * dt  # m

thermal_energy = 0

while t < 12.0 * pi:
    kinetic_energy = 0.5 * m * dot(s.velocity, s.velocity)
    potential_energy = 0.5 * k * dot(s.prev_pos, s.prev_pos)
    thermal_energy += d * dot(s.velocity, s.velocity) * dt

    s.force = -k * s.pos - d * s.velocity + 3.0 * sin(1.0 * t) * vector(1, 0, 0)
    temp = copy(s.prev_pos)
    s.pos, s.prev_pos = 2 * s.pos - s.prev_pos + s.force * dt ** 2 / m, 1 * s.pos
    s.velocity = (s.pos - temp) / (2 * dt)
    spring.axis = s.pos - spring.pos
    t += dt
    rate(1/dt)

    kinetic.plot(pos=(t, kinetic_energy))
    potential.plot(pos=(t, potential_energy))
    thermal.plot(pos=(t, thermal_energy))
    energy.plot(pos=(t, kinetic_energy + potential_energy + thermal_energy))