from vpython import *
import random

ground = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, -1.5, 0))
top = box(color=color.red, size=vector(22, 1, 1), pos=vector(0, 19.5, 0))
left = box(color=color.red, size=vector(1, 22, 1), pos=vector(-11, 9, 0))
right = box(color=color.red, size=vector(1, 22, 1), pos=vector(11, 9, 0))


s = sphere()
s.pos = vector(-10, 0, 0)
s.velocity = vector(5, 19.2, 0)
s.mass = 1.0

k_boltzmann = 1.0
alpha = 0.2


def random_vector():
    return vector(random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1))


def f_langevin(alpha, m, temp, dt):
    return sqrt(2 * alpha * m * temp / dt) * random_vector()


t = 0
dt = 0.001


while t < 20:
    s.accel = f_langevin(alpha, s.mass, 400.0, dt) - alpha * s.velocity * s.mass
    s.velocity += s.accel * dt
    s.pos += s.velocity * dt
    t = t + dt
    rate(abs(1.0 / dt))

    """ bounce off the sides of the box"""
    if not -10.0 < s.pos.x < 10.0:
        s.velocity.x = - s.velocity.x
    if not 0.0 < s.pos.y < 19.0:
        s.velocity.y = - s.velocity.y
    if not 0.0 < s.pos.z < 1.0:
        s.velocity.z = - s.velocity.z
