import matplotlib.pyplot as plt
import numpy as np
import os
    

path = os.path.join(os.path.dirname(__file__), 'caos.txt')
y, x = np.loadtxt(path)

figzoom, axzoom = plt.subplots(figsize=(8,8))

axzoom.set( autoscale_on=False, title='Zoom window')


ang = [2.45, 0.26, 0.849, 0.066]
cons = [1, 4, 0, 1]
for j in range(100):

    for i in range(100):

        a=i*0.01
        alpha = 0.5 + 0.5*a
        axzoom.clear()
        axzoom.scatter(x, y, s=0.1, edgecolors='Black', alpha=alpha)

        
        axzoom.set_xlim(a*ang[0]+cons[0] , cons[1]-a*ang[1])
        axzoom.set_ylim(a*ang[2]+cons[2] , cons[3]-a*ang[3])
        figzoom.canvas.draw()
        plt.pause(0.0001)
    ang = [0.6, 0.12, 0.17, 0.03]
    cons = [3, 3.843, 0.66, 0.956]
    
plt.show()
