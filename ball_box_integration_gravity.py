from vpython import box, sphere, color, vector, rate, dot, graph, gcurve

ground = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, -1.5, 0))
top = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, 19.5, 0))
left = box(color=color.red, size=vector(1, 22, 1), pos=vector(-11, 9, 0))
right = box(color=color.red, size=vector(1, 22, 1), pos=vector(11, 9, 0))

energy = gcurve()
potential = gcurve(color=color.blue)
kinetic = gcurve(color=color.red)

s = sphere()
s.pos = vector(-10, 0, 0)
s.velocity = vector(5, 19.2, 0)
dt = 0.1  # seconds
t = 0
s.oldpos = vector(0, 0, 0)  # m
s.pos = s.oldpos + vector(5, 8, 1) * dt
m = 2  # kg
g = vector(0, -9.8, 0)  # m/s^2
ymax = 20.0
xmax = 20.0
zmax = 20.0

while t < 10:
    # the verlet integration:
    s.force = m * g
    olderpos = s.oldpos
    s.oldpos = 1 * s.pos
    s.pos = 2 * s.pos - olderpos + s.force * dt ** 2 / m
    # work out the energy using a centered derivative
    # for the velocity:
    velocity = (s.pos - olderpos) / (2 * dt)
    kineticEnergy = 0.5 * m * dot(velocity, velocity)
    potentialEnergy = -m * dot(g, s.oldpos + ymax * vector(0, 1, 0))
    print(kineticEnergy + potentialEnergy)
    # Now let’s keep the ball in the box:
    if s.pos.x > xmax or s.pos.x < -xmax:
        s.pos.x, s.oldpos.x = s.oldpos.x, s.pos.x
    if s.pos.y > ymax or s.pos.y < -ymax:
        s.pos.y, s.oldpos.y = s.oldpos.y, s.pos.y
    if s.pos.z > zmax or s.pos.z < -zmax:
        s.pos.z, s.oldpos.z = s.oldpos.z, s.pos.z

    kineticEnergy = 0.5 * m * dot(velocity, velocity)
    potentialEnergy = -m * dot(g, s.pos + ymax * vector(0, 1, 0))
    kinetic.plot(pos=(t, kineticEnergy))
    potential.plot(pos=(t, potentialEnergy))
    energy.plot(pos=(t, kineticEnergy + potentialEnergy))

    t = t + dt
    rate(1 / dt)
