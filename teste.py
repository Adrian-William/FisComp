import numpy as np
import matplotlib.pyplot as plt


def mapa_logistico2(x0, N,M):
    '''
      Calcula e retorna o mapa logistico de uma pupulação de com parametro de crescimento r em um tempo discreto N.

    Argumentos
    ----------
    r : float
        Taxa de crecimento
    x0 : float
        Valor inicial de x
    N : int
        O número de passos.
    M : int
        O numero de passos imprimidos.
    Retorna
    -------
    0
    '''
    y = []
    x = []
    r = 0.001*np.arange(200,dtype=float)+2.1
    t = (np.arange(N,dtype=float))
   
    for j in range(len(r)):

      y.extend(r[j]*np.ones(M))
      a = [x0]
      for i in range(N-1):
       
        a.append(r[j]*a[i]*(1-a[i]))
      
      x.extend(a[-M:]) 
       

    return x,y

plt.figure(figsize=(9,9))
x,y = mapa_logistico2(0.5,200,100)

plt.scatter(y,x , s=0.001 )
plt.ioff()
plt.show()