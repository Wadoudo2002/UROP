import rebound
import numpy as np

sim = rebound.Simulation()

total_sim_time = 100e6*2*np.pi
interval_sim = 10e3*np.pi*2

sim.add(m=1.127,r=0.006257,hash="Star_1")
sim.add(m=0.313,a=0.1321,r=0.001437,omega = 2.05549,e=0.155522,hash = "Star_2")

sim.add(m=6.546e-5, e=0.0880, r=0.0002919, a=0.4607,  hash = "Planet b",inc=0.98*np.pi/180,Omega = 0.87*np.pi/180)
sim.add(m=0.0001958,r=0.0001998,a=0.794,e=0.16,omega = 3.84,hash = "Planet c")

sim.move_to_com()
sim.collision = "direct"
sim.collision_resolve = "merge"

sim.automateSimulationArchive("TOI.bin", interval= interval_sim,deletefile=True)
sim.integrate(total_sim_time)