from pyevtk.hl import gridToVTK 
import numpy as np 
import random as rnd
import h5py

p =3

for p in range(1, 20, 1):
    file = h5py.File("analysis_s"+str(1)+".h5", "r")
    r = file['scales/r/1.0'].value[()]
    θ = file['scales/θ/1.0'].value[()]
    θ[-1] = θ[0]  
    

    u=file['tasks/u']
    print(u.shape)
    nx = len(r); ny = len(r); nz=1
    x = np.zeros((nx, ny, nz)) 
    y = np.zeros((nx, ny, nz))
    z = np.zeros((nx, ny, nz))

    psi =  np.zeros((nx, ny, nz))
    u1 = np.zeros((nx, ny, nz))

    # Multiply by sin theta
    for k in range(nz):
        for i in range(nx):
            for j in range(ny):
                u1[i,j,k] = u[p,i,j]*np.sin(θ)[i]

    for k in range(nz):
        for j in range(ny):
            for i in range(nx): 
                x[i,j,k] = r[j]*np.cos(θ[i]) 
                y[i,j,k] = r[j]*np.sin(θ[i])            
                psi[i,j,k] = u1[i,j,k]


    gridToVTK("./proc-0.000"+str(p), x, y, z, cellData = {"psi" : psi})
    print(p)
