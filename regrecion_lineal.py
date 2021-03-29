###
import numpy as np
import matplotlib.pyplot as mt
def ingrese_numero(mensaje):  #funcion para ingresar un numero positivo
    numero=int(input(mensaje))
    while numero<0:
        numero=int(input(mensaje))
    return numero
def mayor_numero(x):
    mayor=0
    for i in range(len(x)-1):
        if x[i+1]>=x[i]:
            mayor=x[i+1]    
    return mayor    
cantidad=ingrese_numero("Ingrese cantidad: ")
x=[0]*cantidad
y=[0]*cantidad
xy=0
xx=0
xmedio=0
ymedio=0
a=0
b=0
for i in range(cantidad):
    x[i]=ingrese_numero("Ingrese x: ")
    y[i]=ingrese_numero("Ignrese y:")
for i in range(len(x)):
    xmedio=x[i]+xmedio#sumatoria de x
    ymedio=y[i]+ymedio#sumatoria de y
    xy=x[i]*y[i]+xy   #sumatoria de x*y
    xx=x[i]**2+xx     #sumatoria de x al cuadrado
ymedio=ymedio/(i+1)#la media de y 
xmedio=xmedio/(i+1)#la media de x
b=(xy-xmedio*ymedio*(i+1))/(xx-(i+1)*xmedio**2)#calcular la constante b 
a=ymedio-b*xmedio#calcular la constante a
print(xmedio)
print(ymedio)
print(a)
print(b)
numero=np.arange(0,mayor_numero(x)*1.5,0.1)
resultado=a+b*numero
mt.plot(x,y,'o')
mt.plot(numero,resultado)
mt.show()
