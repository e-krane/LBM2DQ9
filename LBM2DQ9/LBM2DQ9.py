import numpy as np
##### Flow definition ###############################################
# This is my first Lattice-Boltzmann code, based on www.palabos.org
# D2Q9 model of flow around a cylinder with uniform cartesian grid
# Author: Erik Krane

#---------------- Problem definition ----------------#
Re = 220.0                      # Reynolds number
nx = 50; ny = 20;               # Domain size
q = 9                           # Lattice size
cylX = nx/4; cylY = ny/4;       # Cylinder coordinates
cylR = ny/9                     # Cylinder radius
uLB = 1.0                       # Lattice velocity
nuLB = uLB*cylR/Re              # Lattice viscosity
omega = 1.0/(3.0*nuLB + 0.5)    # Relaxation parameter

#---------------- Lattice constants ----------------#
c = np.array([(x,y) for x in [0,-1,1] for y in [0,-1,1]])       # Lattice velocities
t = np.array([4/9,1/9,1/9,1/9,1/9,1/36,1/36,1/36,1/36], dtype=float)
print c 
