from vpython import sphere, vector, sin, cos, rate, pi, cross, curve, color

B = vector(0, 0, 5e-4)
q = -1.6e-19
m = 9e-31

s = sphere(radius=2.0e-7)
t = 0  # seconds
dt = 1e-12  # seconds
s.velocity = vector(100, 0, 0)
trail = curve(color=color.blue, pos=s.pos)

while t < 3e-6:
    s.acceleration = q * cross(s.velocity, B)/m
    s.velocity += s.acceleration * dt
    s.pos += s.velocity * dt
    trail.append(s.pos)
    t = t+dt
    rate(4e-7/dt)