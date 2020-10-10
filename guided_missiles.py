from vpython import sphere, vector, rate


def get_velocity(m, target):
    direction = target.r - m.r
    velocity = direction.norm() * 5
    return velocity

missiles = [sphere(pos=vector(0, 0, 0)),
            sphere(pos=vector(0, 100, 0)),
            sphere(pos=vector(100, 100, 0)),
            sphere(pos=vector(100, 0, 0))
            ]

t = 0
dt = 0.001

while t < 100:
    for i, m in enumerate(missiles):
        velocity = get_velocity(m, missiles[(i+1) % 4])
        m.pos += velocity * dt
    t += dt
    rate(1/dt)