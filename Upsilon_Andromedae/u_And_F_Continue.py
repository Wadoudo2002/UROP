import rebound
import numpy as np

sim = rebound.Simulation("u_And_Forwards.bin")

total_sim_time = 1e6*np.pi*2
interval_sim = 1e3*np.pi*2

sim.automateSimulationArchive("u_And_Forwards.bin", interval= interval_sim,deletefile=False)

sim.integrate(sim.t+total_sim_time)