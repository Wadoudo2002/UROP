import rebound
import numpy as np

sim = rebound.Simulation()

total_sim_time = -1e6*np.pi*2
interval_sim = 1e3*np.pi*2

sim.add(m=1.27,hash="u And A")

sim.add(m=0.0016228,a=0.0594, e=0.022, inc=0.419, omega = 0.77, hash = "u And b (Saffar)")
sim.add(m=0.013345,a=0.829, e=0.260, inc=0.138, omega = 4.322, hash = "u And c (Samh)")
sim.add(m=0.0097845,a=2.530, e=0.299, inc=0.415, omega = 4.416, hash = "u And d (Majriti)")

sim.add(m=0.2,a=750,hash = "u And D")

sim.automateSimulationArchive("u_And_Backwards.bin", interval= interval_sim,deletefile=True)
sim.integrate(total_sim_time)