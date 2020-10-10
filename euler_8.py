from vpython import sphere, vector, sin, cos, rate, pi

s = sphere()
t = 0  # seconds
dt = 0.001  # seconds
R = 10  # meters
omega = 3.14  # radians/second

s.pos = vector(R * cos(t * omega), R * sin(t * omega * 2), 0)
s.velocity = omega * R * vector(-sin(t*omega), cos(t * 2 * omega) * 2, 0)

while t < 100 * 2 * pi / omega:
    s.velocity = omega * R * vector(-sin(t*omega), cos(t * 2 * omega) * 2, 0)
    s.pos += s.velocity * dt
    t += dt
    rate(1 / dt)