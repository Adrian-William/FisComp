import numpy as np
import matplotlib.pyplot as plt
import os

#carregando os dados
file_path = os.path.join(os.path.dirname(__file__), 'caos.npz')
data = np.load(file_path)
x = data['x']
y = data['y']

#plotando os pontos
plt.ion()
plt.scatter(x,y,s=0.01,c='Black',alpha=0.2)
plt.show(block=True)

