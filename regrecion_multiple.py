import numpy as np
cant=3#cantidad de casas
precio=[0]*cant#vector precio de longitud cantidad
habitaciones=[0]*cant#vector habitaciones de longitud cantidad
metro=[0]*cant##vector precio de longitud cantidad
for i in range(len(precio)):
    precio[i]=int(input("Ingrese precio:"))#ingresar precio en consola
    habitaciones[i]=int(input("Ingrese habitaciones:"))#ingresar habitaciones en consola
    metro[i]=int(input("Ingrece metroscuadrados:"))#ingresar metro
xt=np.array([[1]*cant,habitaciones,metro])#matriz transpuesta de x
x=np.transpose(xt)#tranpuesta de xt que da x
yt=np.array([precio])#y tranpuesta
y=np.transpose(yt)#tranpuesta de yt es y
p=np.linalg.linalg.inv(xt@x)@xt@y#la matriz inversa de xt*x multiplicado con xt*y
hab=int(input("Ingrese habitacion:"))#ingrese un valor de habitacion para que devuelva un valor precio
met=int(input("Ingrese metro:"))#ingrese un valor de metro para que devuelva un valor precio
print(p[0]+p[1]*in_hab+p[2]*in_met)#imprime el precio de la formula regrecion multiple
