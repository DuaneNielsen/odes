from vpython import sphere, vector, sin, cos, rate, pi
s = sphere()
t = 0  # seconds
dt = 0.001  # seconds
R = 10  # meters
omega = 3.14  # radians/second

s.pos = vector(R * cos(omega * t), R * sin(omega * t), 0)
s.velocity = omega * R * vector(-sin(t * omega), cos(t * omega), 0)

while t < 2 * 2 * pi / omega:
    s.accel = omega ** 2 * R * vector(- cos(omega * t), - sin(omega * t), 0)
    s.velocity += s.accel * dt
    s.pos += s.velocity * dt
    t = t + dt
    rate(1 / dt)
