#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:39:27 2023

@author: wadoudcharbak
"""

import time
start = time.time()

import rebound
import numpy as np
import matplotlib.pyplot as plt

Distance = 2.25
name = "Stability_Test_%.2fAU.bin" % Distance
sa = rebound.SimulationArchive(name)

Number_Of_Frames = 1000

sim = sa[1]

sim.collision = "direct"
sim.collision_resolve = "halt"
sim.exit_max_distance = 40

box = 4

fig1 = rebound.OrbitPlot(sim,particles=[2], primary=sim.particles[0], orbit_style=None, unitlabel="[AU]",color=True,xlim = (-box,box),ylim=(-box,box),figsize = (6,6))
fig1.particles.set_color(["green"])
fig2 = rebound.OrbitPlot(sim, particles = [1], orbit_style=None,show_primary=False, fig=fig1.fig, ax = fig1.ax, periastron=True)
fig2.particles.set_color(["blue"])



counter = 0

for i in range(Number_Of_Frames):
    try:
        sim.integrate(sim.t+10/365.25*np.pi*2)
        fig1.update()
        fig2.update()
        fig1.fig.savefig("/Users/wadoudcharbak/Downloads/Images/out_%02d.png"%i,dpi = 300)
        counter += 1
    except:
        pass



import imageio

#frames = []

writer = imageio.get_writer('Test - %.2f - PType_Ppio2.mp4' % Distance, fps=60)

for i in range(counter):
    #if i % 2 == 0:
    #    continue
    image = imageio.v2.imread("/Users/wadoudcharbak/Downloads/Images/out_%02d.png"%i)
    writer.append_data(image)
    #frames.append(image)
    
writer.close()
'''   
imageio.mimsave('Test - %.2f - PType_R0.gif' % Distance, # output gif
                frames,          # array of input frames
                duration = 20)         # in ms
'''
print('It took', time.time()-start, 'seconds.')