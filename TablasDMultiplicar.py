##Crear un programa que permita ingresar un número entero positivo(N) y otro número también
##entero positivo (M). Luego calcular las tablas de multiplicación desde N a M
##Asumir que M siempre va ser mayor a N.
##Ejemplo:
#Entrada del programa:
#N = 2
#M = 10
#Salida del programa:
#2 x 2 = 4 
# 2 x 3 = 6
#2 x 10 = 20

n = int(input("Ingrese un numero: "))
m = int(input("Ingrese otro numero: ")) 
if ((n >= 0) and(m >= 0)):
    for i in range (1,m):
        print( n,"x",i," = ",i*n)