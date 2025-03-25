import numpy as np
import matplotlib.pyplot as plt

import os

file_path = os.path.join(os.path.dirname(__file__), 'caos.npz')
data = np.load(file_path)
x = data['x']
y = data['y']

color = np.ones(len(x))

print(len(x))
print(len(y))
plt.ion()
plt.scatter(x,y,s=0.01,c='Black',alpha=0.05)
plt.show(block=True)

