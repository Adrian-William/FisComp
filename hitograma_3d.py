import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt


def desvio(X):

    m = len(X)
    
    x = np.median(X ,axis=0)
    z = np.ones(len(x))
    deltax = []
    for i in range(m):
        deltax.append(x)

    return deltax ,x



def random_walk(n,p):
    
    rng = np.random.default_rng()

    lista = rng.choice(a=[-1,1],size=n,p=[1-p, p])
    caminho = np.cumsum(lista)
    tempo = np.arange(0,n,1)
    return caminho, tempo


Y1= []
for i in range(1000):
    x,y1= random_walk(1000,0.6)
    Y1.append(y1)

z,y = desvio(Y1)
print(z)
fig = go.Figure(data=go.Surface(x=x,y=y, z=z, colorscale='Viridis', cmin=0, cmax=1))
fig.show()