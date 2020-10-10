from vpython import *

# box
cylinder(pos=vector(0, 0, 0), axis=vector(15, 0, 0))
cylinder(pos=vector(15, 0, 0), axis=vector(0, 10, 0))
cylinder(pos=vector(15, 10, 0), axis=vector(-15, 0, 0))
cylinder(pos=vector(0, 10, 0), axis=vector(0, -10, 0))

# extrude
cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 5))
cylinder(pos=vector(15, 0, 0), axis=vector(0, 0, 5))
cylinder(pos=vector(15, 10, 0), axis=vector(0, 0, 5))
cylinder(pos=vector(0, 10, 0), axis=vector(0, 0, 5))

# cap
cylinder(pos=vector(0, 0, 5), axis=vector(15, 0, 0))
cylinder(pos=vector(15, 0, 5), axis=vector(0, 10, 0))
cylinder(pos=vector(15, 10, 5), axis=vector(-15, 0, 0))
cylinder(pos=vector(0, 10, 5), axis=vector(0, -10, 0))
