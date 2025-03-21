import functools

import matplotlib.pyplot as plt
import numpy as np
import os

from matplotlib.patches import Rectangle

path = os.path.join(os.path.dirname(__file__), 'caos.txt')
y, x = np.loadtxt(path)
color = np.ones(len(x))

Rectangle = functools.partial(Rectangle, edgecolor='r', facecolor='none')

plt.ion()
plt.scatter(x,y,s=0.01,c=color,alpha=1)
plt.show()
plt.pause(10)
plt.show()