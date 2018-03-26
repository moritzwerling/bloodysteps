import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import plot_vehicle as pv

f10_mat = sio.loadmat("f10.mat")

vehicle = f10_mat['vehicle'][0][0]

wheel1 = vehicle[0][0][0][0]
wheel2 = vehicle[1][0][0][0]
wheel3 = vehicle[2][0][0][0]
wheel4 = vehicle[3][0][0][0]
chassi = vehicle[4][0][0][0]
windwhield = vehicle[5][0][0][0]
rearwindow = vehicle[6][0][0][0]

geometries = {'wheel1': wheel1, 'wheel2': wheel2,
              'wheel3': wheel3, 'wheel4': wheel4,
              'chassi': chassi, 'windshield': windwhield,
              'rearwindow': rearwindow}

np.save('f10', geometries)

fig, ax = plt.subplots()
t = np.arange(0.0, 10.0, 0.01)
plt.plot(t,np.sin(t))

plt.show

x = 0
y = 0
psi = np.pi/4
delta = -np.pi/8
length = 10
width = 2

pv.plot_vehicle(ax, x, y, psi, delta, length, width)

plt.axis('equal')
plt.show()

