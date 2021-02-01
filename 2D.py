import numpy as np
import matplotlib.pyplot as plt 
import math as mt


#creacion de el Lienzo
plt.axis([-20, 20, -20, 20])

#Declaracion de variables
LL= 10
LC=5
#creacion del rectangulo
plt.text(-(LL), LC, 'Lado Largo = 20 unidades')
plt.plot([-(LL), LL], [-(LC), -(LC)], linewidth=2)

plt.plot([10, 10], [5, -5], linewidth=2)
plt.text(10, 0, 'Lado Chico = 10 unidades')
plt.plot([-10, -10], [-5, 5], linewidth=2)

plt.plot([10, -10], [5, 5], linewidth=2)
plt.axes().set_aspect('equal')

#creacion del circulo grande
xcenter = 10
ycenter = 5
radioL = 10
radioC = radioL/2

alpha1 = mt.radians(0)
alpha2 = mt.radians(360)
difalpha = mt.radians(2)



for alpha in np.arange(alpha1, alpha2, difalpha):
    x=xcenter+radioL*mt.cos(alpha)
    y=ycenter+radioL*mt.sin(alpha)
    plt.scatter(x, y, s=7, color='b')

#creacion del circulo chico
for alpha in np.arange(alpha1, alpha2, difalpha):
    x=xcenter+radioC*mt.cos(alpha)
    y=ycenter+radioC*mt.sin(alpha)
    plt.scatter(x, y, s=7, color='r')


#creacion de flechas
plt.arrow(10, 5, 3, 0, head_length=2, head_width=2)
plt.arrow(10, 5, 0, 8, head_length=2, head_width=2)  

#Textos
plt.text(-(10), -10, 'Flecha 1 = 10 unidades = Lado largo/2')
plt.text(-(10), -12, 'Flecha 2 = 5 unidades= Lado Largo/4')
plt.text((11.6), 6.1, '2')
plt.text(10.3, 11.6, '1')








plt.show()