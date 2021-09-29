"""
Computes Bfield in Schwarzchild background

"""

import numpy as np
import time
import matplotlib.pyplot as plt
import subprocess
import pathlib
import h5py

from dedalus import public as de
from dedalus.extras.plot_tools import quad_mesh, pad_limits
from dedalus.tools  import post
from dedalus.tools import post

import logging
logger = logging.getLogger(__name__)

# parameters
nr = 128
nθ = 128

# Outer and inner radius of Black hole
R_in = 2.1
R_out = 10


# Bases and domain
r_basis = de.Chebyshev('r',nr, interval=[R_in, R_out], dealias=3/2)
θ_basis = de.Fourier('θ',nθ,  dealias=3/2)

domain = de.Domain([θ_basis, r_basis], grid_dtype=np.float64)

# Potential
def V(*args):
    r=args[1].data
    return (2.0/pow(r,2))*(1.0-2.0/r)

def Potential(*args, domain=domain, F=V):
    """
    This function takes arguments *args, a function F, and a domain and
    returns a Dedalus GeneralFunction that can be applied.
    """
    return de.operators.GeneralFunction(domain, layout='g', func=F, args=args)

# Now we make it parseable, so the symbol BF can be used in equations
# and the parser will know what it is.
de.operators.parseables['Vr'] = Potential

# Problem
problem = de.IVP(domain, variables=['u', 'u_t', 'ur'])
problem.meta[:]['r']['dirichlet'] = True
problem.add_equation("-dt(u_t) - (4.0/pow(r,3))*(1.0-2.0/r)*ur + pow(1.0-2.0/r,2)*dr(ur) = Vr(t,r)*u")
problem.add_equation("u_t - dt(u) = 0")
problem.add_equation("ur - dr(u) = 0")

# note that we apply the right() operator to the forcing
problem.add_bc("left(u_t)=left((1.0-2.0/r)*ur)")
problem.add_bc("right(u)=1.0")

# Build solver
solver = problem.build_solver(de.timesteppers.RK443)
solver.stop_sim_time = 10
solver.stop_wall_time = np.inf
solver.stop_iteration = np.inf

# Reference local grid and state fields
r = domain.grid(1)
u = solver.state['u']
ur = solver.state['ur']

# Setup smooth triangle with support in (-1, 1)
u['g'] = 1
u.differentiate('r', out=ur)

#analysis
analysis = solver.evaluator.add_file_handler('analysis',iter=50, max_writes=50)
#analysis.add_task("u", name='<u>')

analysis.add_system(solver.state)

# run simulation
import time

# Main loop
dt = 1e-2
start_time = time.time()
while solver.ok:
    solver.step(dt)
    if solver.iteration % 100 == 0:
        print('Completed iteration {}'.format(solver.iteration))
end_time = time.time()
print('Runtime:', end_time-start_time)

# file arrangement 
import subprocess
print(subprocess.check_output("find analysis", shell=True).decode())

