
a = int(input("Ingrese Primer Numero: "))
b = int(input("Ingrese Segundo Numero: "))
c = int(input("Ingrese Tercer Numero: "))
d = int(input("Ingrese Cuarto Numero: "))
e = int(input("Ingrese Quinto Numero: "))

if (a == b) or (a == c) or (a == d) or (a == e):
    print("Hay Duplicados")
elif (b == c) or (c == d) or (d == e) or (b == a):
    print("Hay Duplicados")
elif (c == a) or (c == b) or (c == d) or (c == e):
    print("Hay Duplicados")
elif( d == a) or (d == b) or ( d == c) or (d == e):
    print ("Hay Duplicados")
elif (e == a) or (e == b) or ( e == c) or (e == d):
    print("Hay Duplicados")
else:
    print ("No Hay Duplicados")