from vpython import sphere, box, cylinder, cone, color, curve, rate
from vpython import sqrt, atan, cos, sin, pi
from vpython import vector as vec

dirt = vec(1, 0.6, 0.4)

ground = box(color=dirt)
ground.axis = vec(1, 0, 1)
ground.size = vec(0.305 * 120 / sqrt(2), 0.305 * 1, 0.305 * 120 / sqrt(2))
ground.pos = 0.305 * vec(0, -0.5, 0)

mound = cone(color=dirt)
mound.axis = 0.305 * vec(0, 10 / 12, 0)
mound.radius = 0.305 * 9

pitcher = cylinder(color=color.red)
pitcher.pos = 0.305 * vec(0, 10 / 12, 0)
pitcher.axis = 0.305 * vec(0, 6, 0)

plate = box(color=color.yellow)
plate.size = vec(1, 0.1, 1)
plate.pos = 0.305 * vec(60.5, 0, 0)

strikezone = box(color=color.red)
strikezone.size = vec(0.305 / 12, 0.305 * 2, 0.305 * 2)
strikezone.pos = 0.305 * vec(60.5, 2.5, 0)


def in_boundary(x, bound, pos):
    return x - bound/2 < pos < x + bound/2


def in_strikezone():
    return in_boundary(strikezone.pos.x, strikezone.size.x, ball.pos.x) and \
           in_boundary(strikezone.pos.y, strikezone.size.y, ball.pos.y) and \
           in_boundary(strikezone.pos.z, strikezone.size.z, ball.pos.z)


gravity = 0.447 * vec(0, -9.8, 0)

ball = sphere()
ball.pos = 0.305 * vec(0, 5 + (10 / 12), 0)
ball.radius = 0.305 * 1.45 / 12
angle = atan((strikezone.pos.y - ball.pos.y) / (strikezone.pos.x - ball.pos.x)) + 0.03
ball.velocity = 0.447 * 120 * vec(cos(angle), sin(angle), 0)

trail = curve(color=color.blue, pos=ball.pos)

t = 0
dt = 0.0001
C = 1.0
A = ball.radius ** 2 * pi
p = 1.2

wind = vec(0, 0, 40)


def drag(v, C, p, A):
    return 0.5 * C * p * A * v.mag * v


def ball_drag(v):
    return drag(v, C, p, A)


while ball.pos.mag < strikezone.pos.mag:
    ball.acceleration = gravity - ball_drag(ball.velocity) + ball_drag(wind)
    ball.velocity += ball.acceleration * dt
    ball.pos += ball.velocity * dt
    trail.append(ball.pos)
    if in_strikezone():
        strikezone.color = color.green
    t += dt
    rate(1 / dt)
