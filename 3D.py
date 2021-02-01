import numpy as np
import matplotlib.pyplot as plt 
import math 


print("Por favor proporcione las cordenadas del hit point")
print("Comencemos con la x")
x=float(input())
print("ahora la y")
y=float(input())

#creacion de el Lienzo
plt.axis([0, 100, 0, 100])



#creacion de A
plt.plot([40, 30], [60, 10], linewidth=5, color='r')
plt.plot([30, 80], [10, 60], linewidth=5, color='r')
plt.plot([80, 40], [60, 60], linewidth=5, color='r')

#Creacion de A1
plt.plot([x, 40], [y, 60], linewidth=5, color='b')
plt.plot([x, 30], [y, 10], linewidth=5, color='b')

#creacion de A2
plt.plot([x, 80], [y, 60], linewidth=5, color='b')
plt.plot([x, 30], [y, 10], linewidth=5, color='b')


#para determinar la distancia entre cada punto
#distancia entre el punto 0 a 1
#formare un triangulo rectangulo para calcular su dictancia a traves de pitagoras
#0=(40,60) 1=(30,10) punto imaginario (30,60)
#formula C2 = reiz(a2 + b2)
#la distancia es igual a 51

#el proceso es el mismo para los demas
#del 1 al 2 hay 40 unidades
#del 2 al 0 hay 50 unidades

s = float((51+40+50)/2)
print(s)
Temp=float(((s)*(s-51)*(s-40)*(s-50)))
print (Temp)
A1=float(math.sqrt(Temp))
print (A1)

#buscar el area del segundo triangulo
#lado 1
#creacion de los catetos imaginarios
plt.text(x, 10, '.')
LadoA1=float(y-10)
LadoA2=float(x-30)
#calculo de la hipotenusa
c=float()
c=math.sqrt((LadoA1*LadoA1)*(LadoA2*LadoA2))
print('c')
print(c)

#lado 2
#creacion de los catetos imaginarios
plt.text(40, y, '.')
LadoA11=float(60-y)
LadoA21=float(x-40)
#calculo de la hipotenusa
c1=float()
c1=math.sqrt((LadoA11*LadoA11)*(LadoA21*LadoA21))
print('c1')
print(c1)
#buscar el area del segundo triangulo

s2 = float((51+c+c1)/2)
print('s2')
print(s2)
Temp2=float(((s2)*(s2-51)*(s2-c)*(s2-c1)))
print(Temp2)






plt.show()