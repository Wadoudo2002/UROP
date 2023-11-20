import rebound
import numpy as np


sim = rebound.Simulation("TOI.bin")

total_sim_time = 10e6*np.pi*2
interval_sim = 1e3*np.pi*2

sim.automateSimulationArchive("TOI.bin", interval= interval_sim,deletefile=False)

sim.integrate(sim.t+total_sim_time)