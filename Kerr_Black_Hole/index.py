# %%
import matplotlib.pyplot as plt 
import numpy as np 
from ipywidgets import interact, interactive, fixed, interact_manual
from scipy.integrate import odeint

def model(z,t,beta,theta):
    
    y1 = z[0]
    y2 = z[1]
    dy1dt = y2
    dy2dt = 1-y1*np.sin(theta)**2+beta*y1**2*np.sin(theta)**2
    dzdt = [dy1dt,dy2dt]
    return dzdt


r=1.5
theta = np.linspace(-np.pi,np.pi,10000)
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

  # Data for a three-dimensional line
  zline = theta
  z1 = data
  ax.plot3D(np.cos(phi)/(z1[0][:,0]), np.sin(phi)/(z1[0][:,0]), zline, 'gray')
  ax.hold(True)
  ax.plot3D(np.cos(phi)/(z1[3][:,0]), np.sin(phi)/(z1[3][:,0]), zline, 'gray')
  ax.hold(True)
  ax.plot3D(np.cos(phi)/(z1[5][:,0]), np.sin(phi)/(z1[5][:,0]), zline, 'gray')
  ax.hold(True)
  ax.plot3D(np.cos(phi)/(z1[10][:,0]), np.sin(phi)/(z1[10][:,0]), zline, 'gray')
# %%
beta2=0.03
data = mapeado(z0,phi,beta2,theta)
graficado(data,theta)
# %%
