import matplotlib.pyplot as plt
import numpy as np
import os
import time
    
file_path = os.path.join(os.path.dirname(__file__), 'caos.npz')
data = np.load(file_path)
x = data['x']
y = data['y']
figzoom, axzoom = plt.subplots(figsize=(8,8))

axzoom.set( autoscale_on=True, title='Zoom window')


ang = [2.472, 0.37, 0.8573, 0.0948]
cons = [1, 4, 0, 1]
init = [100,0.01]
t = lt =0
fps = 1/30
for j in range(10):

    for i in range(init[0]):
        t = time.thread_time()
        daltat = t-lt
        lt = t
        print(daltat)
        a=i*init[1]
        alpha = 0.1 + 0.5*a
        axzoom.clear()
        axzoom.scatter(x, y, s=0.1, edgecolors='Black', alpha=alpha)       
        axzoom.set_xlim(a*ang[0]+cons[0] , cons[1]-a*ang[1])
        axzoom.set_ylim(a*ang[2]+cons[2] , cons[3]-a*ang[3])
        figzoom.canvas.draw()
        if daltat < fps:
            frame = fps-daltat
        else:
            frame = fps
        plt.pause(fps)
    ang = [0.45, 0.24, 0.17, 0.03]
    cons = [3, 3.843, 0.66, 0.96]
    init = [50,0.02]
plt.show() 
'''
axzoom.scatter(x, y, s=0.1, edgecolors='Black', alpha=0.1)  
for i in range(init[0]):
    a=i*init[1]
    axzoom.set_xlim(a*ang[0]+cons[0] , cons[1]-a*ang[1])
    axzoom.set_ylim(a*ang[2]+cons[2] , cons[3]-a*ang[3])
    figzoom.canvas.draw()
    plt.pause(0.1)
plt.show()
'''