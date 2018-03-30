import matplotlib.pyplot as plt
from matplotlib.patches import Circle


class KammsCircle(object):
    def __init__(self, ax, a_max=10):
        c = Circle((0, 0), a_max, color='grey')
        ax.add_patch(c)
        self.acc = plt.Line2D([], [], color='k', marker='P')
        ax.add_line(self.acc)

    def update(self, a_vec):
        self.acc.set(xdata=[0, a_vec[0]], ydata=[0, a_vec[1]])


fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')

kc = KammsCircle(ax1)
kc.update((5, 5))
plt.margins(.5)
plt.show()
