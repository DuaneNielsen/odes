from vpython import *

""" estimate the derivative of sine numerically """

error = gcurve()


def dsin(x, dx):
    return (sin(x + dx/2) - sin(x - dx/2)) / dx


x = 0.1
dx = 1

while dx > 1e-14:
    error.plot(pos=(log10(dx), log10(abs(dsin(x, dx) - cos(x)))))
    dx = dx/1.1
