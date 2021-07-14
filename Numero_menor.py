# Se pide realizar una función que devuelva el número enteros más pequeño de un listado 
# ingresado por el usuario,
#  tal que la suma de los N números exceda un valor pasado por parámetro en la función
def sumadora (lista:list)->int:
    sumar = 0
    for i in range (len(lista)):
        sumar += i
    return sumar

def numeroPequeño(lista:list,valor:int)->int: 
    menor = 0
    suma = sumadora(lista)
    fin = True
    while fin:
        if suma >= valor:
            for i in lista:
                if menor == 0:
                    menor=i
                else:
                    if i < menor:
                        menor = i
            fin= False
        else:
            nuevoValor= int(input("Ingrese un nuevo valor: "))
            valor = nuevoValor
            fin = True

    print(menor)
    return menor



lista = [1,2,4,5,6]
valor = 8
numeroPequeño(lista,valor)