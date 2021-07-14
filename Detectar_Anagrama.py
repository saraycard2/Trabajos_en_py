
# 5) Escribir un programa que primero solicite una palabra al usuario y 
# luego le permita al usuario ingresar 5 palabras.
# El sistema deberá calcular cuántas y cuáles palabras de las 5 ingresadas 
# pueden escribirse exactamente con las letrasde la palabra ingresada al principio 
# (utilizando todas las letras y sin repetir ninguna). 
# Ej: Palabra inicial: CASO5 palabras: MAMA, CLASE, SACO, COSA, PEPEEL sistema deberá 
# devolver 2 palabras (SACO y COSA).. 
def dectPalabras (PalabraInicial:str,listaPalabras:str)->str:
    palabras = sorted(PalabraInicial)
    anagrama = []
    #anagrama = [i for i in listaPalabras if sorted(i)== palabras]
    for i in listaPalabras:
        if sorted(i) == palabras:
            anagrama.append(i) 

    cadenaLista = ','.join(str(i) for i in anagrama)
    print(cadenaLista)
    print(type(cadenaLista))
    return cadenaLista

    
    
    



def main ()->None:
    palabraInicial= input("Ingrese palabra inicial: ")
    palabra1= input("Ingrese primera palabra: ")
    palabra2=input("Ingrese segunda palabra: ")
    palabra3=input("Ingrese tercera palabra: ")
    palabra4= input("Ingrese cuarta palabra: ")
    palabra5= input("Ingrese quinta palabra: ")
    lista = [palabra1,palabra2,palabra3,palabra4,palabra5]
    dectPalabras(palabraInicial,lista)

main()
