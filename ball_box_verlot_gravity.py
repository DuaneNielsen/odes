from vpython import box, sphere, color, vector, rate, dot, graph, gcurve
import copy

ground = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, -1.5, 0))
top = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, 19.5, 0))
left = box(color=color.red, size=vector(1, 22, 1), pos=vector(-11, 9, 0))
right = box(color=color.red, size=vector(1, 22, 1), pos=vector(11, 9, 0))

energy = gcurve()
potential = gcurve(color=color.blue)
kinetic = gcurve(color=color.red)

dt = 0.1

g = 9.8
s = sphere()
s.pos = vector(-7, 10, 0)
#s.velocity = vector(5, 19.2, 0)
s.velocity = vector(0, 0, 0)
s.prev_pos = s.pos - (s.velocity * dt)
s.accel = vector(0, -g, 0)
s.mass = 2.0

t = 0

while t < 10:

    kinetic_energy = 0.5 * s.mass * dot(s.velocity, s.velocity)
    potential_energy = s.mass * 9.8 * dot(s.pos, vector(0, 1, 0))
    kinetic.plot(pos=(t, kinetic_energy))
    potential.plot(pos=(t, potential_energy))
    energy.plot(pos=(t, kinetic_energy + potential_energy))

    temp_pos = copy.copy(s.pos)
    s.pos = 2 * s.pos - s.prev_pos + s.accel * dt ** 2
    s.prev_pos = temp_pos
    s.velocity = (s.pos - s.prev_pos) / dt
    t += dt
    rate(abs(1.0 / dt))

    if not -10.0 < s.pos.x < 10.0:
        s.pos.x, s.prev_pos.x = - s.pos.x, - s.prev_pos.x
    if not 0.0 < s.pos.y < 19.0:
        s.pos.y, s.prev_pos.y = - s.pos.y, - s.prev_pos.y,

