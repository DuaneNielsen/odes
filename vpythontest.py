from vpython import *


a = vector(1,2,0)
b = vector(2,2,0)
arrow(axis=a, color=color.blue)
arrow(axis=b, color=color.red)
arrow(axis=cross(a,b))
arrow(axis=cross(b,a), color=color.yellow)