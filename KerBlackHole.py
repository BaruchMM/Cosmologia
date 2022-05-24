#%%
import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import pylab as pl
import numpy as np 
import matplotlib.gridspec as gridspec
from scipy.integrate import odeint

#%%
def model(z,t,beta,theta):
    
    y1 = z[0]
    y2 = z[1]
    dy1dt = y2
    dy2dt = 1-y1+beta*y1**2*np.sin(theta)**2*(1-np.sin(theta)**2)
    dzdt = [dy1dt,dy2dt]
    return dzdt

r=1.5
theta = np.linspace(-20*np.pi,20*np.pi,10000)
phi = np.linspace(-20*np.pi,20*np.pi,10000)
z0 = [1/r,0.]

def mapeado(z0,phi,beta,theta):
  data = []
  for th in theta:
    z = odeint(model,z0,phi,args=(beta,th))
    data.append(z)
  
  return data

def graficado(data,theta):
  ax = plt.axes(projection='3d')
  z1 = data
  # Data for a three-dimensional line
  zline = theta
  xline = np.cos(phi)/(z1[10][:,0])
  yline = np.sin(phi)/(z1[10][:,0])
  ax.plot3D(xline, yline, zline, 'gray')

#%%
beta2=0.03
data = mapeado(z0,phi,beta2,theta)
graficado(data,theta)

#%%
beta1=1.5
beta2=0.5
# Función para resolver las ecuaciones diferenciales ordinarias con las condiciones iniciales z0
z1  = mapeado(z0,phi,beta1,theta)
z2  = mapeado(z0,phi,beta2,theta)

plt.figure(figsize=(8,8))
plt.plot(np.cos(phi)/(z1[10][:,0]),np.sin(phi)/(z1[10][:,0]),'b-',label=r'$\beta =$'+str(beta1))
plt.plot(np.cos(phi)/(z2[12][:,0]),np.sin(phi)/(z2[12][:,0]),'C0--',label=r'$\beta =$'+str(beta2))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.plot(0,0,marker="o", color="orange")
plt.legend()
plt.grid()
plt.axis('square')

plt.show()
# %%
