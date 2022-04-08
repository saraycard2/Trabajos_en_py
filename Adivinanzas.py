print("Bienvenido al Juego")
palabra = input(" Usuario1 Ingrese palabra a adivinar: ")
nroletras = len(palabra)

print("Usuario2 Tiene 3 Intentos para Adivinar")
intento1 = int(input("Ingrese primer intento: "))
intento2 = int(input("Ingrese segundo intento: "))
intento3 = int(input("Ingrese tercer intento: "))

if(nroletras == intento1 and intento1 == intento2 ) or (nroletras == intento1 and intento1 == intento3) or ( nroletras == intento2 and intento2 == intento3):
    print("Ah, pero sos buenisimo")
elif (nroletras == intento1) or (nroletras == intento2) or (nroletras == intento3):
    print("Muy bien")

elif (nroletras != intento1) and (nroletras != intento2) and (nroletras != intento3): 
    print("vuelva prontos, esta vez no se puedo")




