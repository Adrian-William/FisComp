import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('caos.txt')
color = np.ones(len(x))

plt.ion()
plt.scatter(x,y,s=0.01,c=color,alpha=1)
plt.show(1)
