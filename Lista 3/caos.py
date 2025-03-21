import numpy as np
import matplotlib.pyplot as plt

import os

file_path = os.path.join(os.path.dirname(__file__), 'caos.txt')
y, x = np.loadtxt(file_path)
print(file_path)
color = np.ones(len(x))


plt.ion()
plt.scatter(x,y,s=0.01,c=color,alpha=1)
plt.show()
plt.pause(10)
