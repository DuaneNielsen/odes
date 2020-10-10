from vpython import box, sphere, color, vector, rate, dot, graph, gcurve

xmax, ymax = 20, 20

ground = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, -ymax/2, 0))
top = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, ymax/2, 0))
left = box(color=color.red, size=vector(1, 22, 1), pos=vector(-xmax/2, 0, 0))
right = box(color=color.red, size=vector(1, 22, 1), pos=vector(xmax/2, 0, 0))

energy = gcurve()
potential = gcurve(color=color.blue)
kinetic = gcurve(color=color.red)

dt = 0.01
g = 9.8
s = sphere()
s.pos = vector(-7, 1, 0)
s.velocity = vector(5, 19.2, 0)
s.accel = vector(0, -g, 0)
s.mass = 2.0

t = 0

while t < 10.0:

    # compute and graph energy
    kinetic_energy = 0.5 * s.mass * dot(s.velocity, s.velocity)
    potential_energy = s.mass * 9.8 * dot(s.pos + vector(0, ymax/2, 0), vector(0, 1, 0))
    kinetic.plot(pos=(t, kinetic_energy))
    potential.plot(pos=(t, potential_energy))
    energy.plot(pos=(t, kinetic_energy + potential_energy))

    # update time and position
    t += dt
    s.pos += s.velocity * dt + 0.5 * s.accel * dt ** 2
    s.velocity += s.accel * dt
    rate(1/dt)
    print(s.pos)

    # collisions
    if not -xmax/2 < s.pos.x < xmax/2:
        s.velocity.x = - s.velocity.x
    if not -ymax/2 < s.pos.y < ymax/2:
        s.velocity.y = - s.velocity.y