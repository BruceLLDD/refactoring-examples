"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random

boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)





def update_boids(boids):
    # boids_x, boids_y, boid_x_velocities, boid_y_velocities
    bx,by,bxv,byv=boids
    number_boids = len(bx)
    # Fly towards the middle
    for i in range(number_boids):
        for j in range(number_boids):
            bxv[i]=bxv[i]+(bx[j]-bx[i])*0.01/number_boids
    for i in range(number_boids):
        for j in range(number_boids):
            byv[i]=byv[i]+(by[j]-by[i])*0.01/number_boids
    # Fly away from nearby boids
    for i in range(number_boids):
        for j in range(number_boids):
            if (bx[j]-bx[i])**2 + (by[j]-by[i])**2 < 100:
                bxv[i]=bxv[i]+(bx[i]-bx[j])
                byv[i]=byv[i]+(by[i]-by[j])
    # Try to match speed with nearby boids
    for i in range(number_boids):
        for j in range(number_boids):
            if (bx[j]-bx[i])**2 + (by[j]-by[i])**2 < 10000:
                bxv[i]=bxv[i]+(bxv[j]-bxv[i])*0.125/number_boids
                byv[i]=byv[i]+(byv[j]-byv[i])*0.125/number_boids
    # Move according to velocities
    for i in range(number_boids):
        bx[i]=bx[i]+bxv[i]
        by[i]=by[i]+byv[i]
