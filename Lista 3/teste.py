import matplotlib.pyplot as plt
import numpy as np
import os
    

# Fixing random state for reproducibility
path = os.path.join(os.path.dirname(__file__), 'caos.txt')
y, x = np.loadtxt(path)

figzoom, axzoom = plt.subplots(figsize=(5,5))

axzoom.set( autoscale_on=False, title='Zoom window')


axzoom.scatter(x, y, s=0.01, c='b', alpha=1)


for i in range(100):
#    sleep(0.1)
    axzoom.set_xlim(i - 0.1, i + 0.1)
    axzoom.set_ylim(i - 0.1, i + 0.1)
    
    figzoom.canvas.draw()

figzoom.canvas.mpl_connect('button_press_event', on_press)
plt.show()