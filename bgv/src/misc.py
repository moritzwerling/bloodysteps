import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon

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

geo = np.load('f10.npy')[()]

fig, ax = plt.subplots()

patches = []
for key, value in geo.items():
    print(value)
    polygon = Polygon(value, closed=True, alpha = 0.5)
    #plt.plot(value[:, 0], value[:, 1])
    ax.add_patch(polygon)

plt.axis('equal')
plt.show()

