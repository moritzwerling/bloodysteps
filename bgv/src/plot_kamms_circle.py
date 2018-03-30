import matplotlib.pyplot as plt
from matplotlib.patches import Circle


class KammsCircle(object):
    def __init__(self, ax, x=0, y=0, a_max=10):
        self.x = x
        self.y = y
        c = Circle((x, y), a_max, facecolor='grey', edgecolor='k')
        ax.add_patch(c)
        self.acc = plt.Line2D([], [], color='k', marker='P')
        ax.add_line(self.acc)

    def update(self, a_vec):
        self.acc.set(xdata=[self.x, self.x+a_vec[0]], ydata=[self.y, self.y+a_vec[1]])


fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')

kc = KammsCircle(ax1, 3, 5)
kc.update((-2, 5))
plt.margins(.5)
plt.show()
