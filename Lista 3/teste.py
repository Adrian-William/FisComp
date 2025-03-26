
import matplotlib.pyplot as plt
import numpy as np
import os
import time



file_path = os.path.join(os.path.dirname(__file__), 'caos.npz')
data = np.load(file_path)
x = data['x']
y = data['y']
figzoom, axzoom = plt.subplots(figsize=(3,3))

axzoom.set( autoscale_on=True, title='Zoom window')


ang = [2.472, 0.37, 0.8573, 0.0948]
cons = [1, 4, 0, 1]
init = [200,0.005]
t = lt =0
fps = 1/10
c = 41
for j in range(10):

    for i in range(init[0]):
        
        a=i*init[1]
        b=round((c/(1+a*c)))
        xmin =a*ang[0]+cons[0]
        xmax = cons[1]-a*ang[1]
        ymin = a*ang[2]+cons[2]
        ymax = cons[3]-a*ang[3]
        mask =  (y >= ymin) & (y <= ymax) 

        deltax = x[mask]
        deltay = y[mask]
        axzoom.clear()
        axzoom.scatter(deltax[::b], deltay[::b], s=0.1, edgecolors='Black', alpha=0.1)
        axzoom.set_xlim(xmin , xmax)
        axzoom.set_ylim(ymin , ymax)

        t = time.time()
        daltat = t-lt
        lt = t 
        if daltat < fps:
            time.sleep(fps-daltat)
        figzoom.canvas.draw()
        plt.pause(0.001)
     
    ang = [0.4468, 0.223, 0.192, 0.055]
    cons = [3.02, 3.843, 0.66, 0.959]
    init = [20,0.05]
    c = 9
plt.show() 
