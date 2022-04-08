print("Bienvenido")

a = int(input("Ingrese Primer Numero: "))
b = int(input("Ingrese Segundo Numero: "))
c = int(input("Ingrese Tercer Numero: "))
d = int(input("Ingrese Cuarto Numero: "))
e = int(input("Ingrese Quinto Numero: "))

if (a >= b) and (a >= c) and (a >= d) and (a >= e):
    print("El Numero Mayor es: ",a)
elif (b >= a) and (b >= c) and (b >= d) and (d >= e):
    print("El Numero Mayor es: ",b)
elif (c >= a) and (c >= b) and ( c >= d) and (c >= e):
    print("El Numero Mayor es: ",c)
elif (d >= a) and (d >= b) and ( d >= c) and (d >= e):
    print("El Numero Mayor es: ",d)
elif (e >= a) and (e >= b) and ( e >= d) and (e >= c):
    print("El Numero Mayor es: ",e)
print("")
if (a <= b) and (a <= c) and (a <= d) and (a <= e):
    print("El Numero Menor es: ",a)
elif (b <= a) and (b <= c) and ( b <= d) and ( b <= e):
    print("El Numero Menor es: ",b)
elif (c <= a) and (c <= b) and ( c <= d) and (c <= e):
    print("El Numero Menor es: ",c)
elif (d <= a) and (d <= b) and ( d <= c) and (d <= e):
    print("El Numero Menor es: ",d)
elif (e <= a) and (e <= b) and ( e <= d) and (e <= c):
    print("El Numero Menor es: ",e)
