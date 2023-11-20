import rebound
import numpy as np

sim = rebound.Simulation()

def setupSimulation():
    sim = rebound.Simulation()
    sim.add(m=0.957, x=2.0923179e-2,hash="K_47A")
    sim.add(m=0.342,a=0.08145,e=0.0288, omega=3.95 ,hash="K_47B")
    
    sim.add(m=6.21565e-6,a=0.2877,e=0.0210,inc=2.9e-3,omega=0.848 ,hash="Inner_Planet")
    sim.add(m=5.711193e-5,a=0.6992,e=0.024, inc=0.020 , omega=6.14,hash="Middle_Planet")
    sim.add(m=9.51865e-6,a=0.9638,e=0.044,inc=0.024, omega=5.34,hash="Outer_Planet")
    sim.move_to_com()
    
    #sim.move_to_com()
    return sim

sim = setupSimulation()


sim.automateSimulationArchive("K47_1e3_Years.bin", interval=1e3*np.pi*2,deletefile=True)

sim.integrate(1e6*np.pi*2)