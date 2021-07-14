from os import system
import random

def generadorM(size:int)->list:
    '''
    Pre: recibe un numero entero entre 1,2 o 3 que seria el tamaño de la matriz deciada
    Post: devuelve una matriz de numeros pares ordenando al azar las filas
    '''
    lista = generadorL(size)
    contador = 0
    matriz = []
    for i in range(size*4):
        fila = []
        for j in range(size*4):
            if (contador == len(lista)):
                contador = 0
            fila.append(lista[contador])
            contador  += 1
        random.shuffle(fila)
        matriz.append(fila)
    return matriz

def generadorL(size:int)->list:
    '''
    Pre: recibe un numero 
    Post: genera una lista de numeros ordenados al azar 
    '''
    lista = []
    rangoM = (size*4*4*size)//2
    for i in range(rangoM):
        lista.append(i)
    random.shuffle(lista)
    return lista

def generadorMI(size:int)->list:
    '''
    Pre: recibe un numero 
    Post: devuelve una matriz de con el signo "?"
    '''
    matriz = []
    for i in range(size*4):
        fila = []
        for j in range(size*4):
            fila.append("?")
        matriz.append(fila)
    return matriz

def selectCoor(fila: int, col:int, matR:list, matI:list)->None:
    #guarda las coordenada ingresadas y le pasa este dato a la funcion impM para que lo imprima
    valor = matR[fila][col]
    matI[fila][col] = valor
    impM(matI)

def turno(matR:list, matI:list, matR2:list, matI2:list, jugador:str, prob:int, comodines:list, coincidencias:int)->int:
    '''
    Pre: Recibe 2 matrices previamente creadas, junto con los jugadores previamente seleccionados y 
    la probabilidad previamente creada
    Post: recibe las coordenadas y dicta si estan son pares o no, asigna el turno a quien le corresponda y si
    es el caso le da un turno mas, siempre retorna un entero.
    '''
    noAcerto = False
    print("Turno de jugador ",jugador)
    turnoExtra = llamarComodin(matR2, matI2, prob, comodines)
    while not noAcerto:
        fila1 = int(input("ingrese fila: ")) -1
        col1 = int(input("ingrese columna: ")) -1
        selectCoor(fila1, col1, matR, matI)

        fila2 = int(input("ingrese fila: ")) -1
        col2 = int(input("ingrese columna: ")) -1
        selectCoor(fila2, col2, matR, matI)

        if (matR[fila1][col1] == matR[fila2][col2]):
            coincidencias += 1
            print("Bien!")
            if (len(matR)*len(matR)//2 == coincidencias):
                print("felicidades gano el juego")
                input()
                noAcerto = True    
        else:
            noAcerto = True
            matI[fila1][col1] = "?"
            matI[fila2][col2] = "?"
            input("Presina enter para continuar, loser")
            system("cls")
            if (turnoExtra):
                turnoExtra = False
                noAcerto = False

    return coincidencias

def exito(prob:int)->bool:
    '''
    Pre: recibe un entero previamente definido
    Post: retorna una variable booleana que al ser "True" va hacia "llamarComodin" para
    asignar un comodin al azar
    '''
    exito = False
    if (random.randint(1, prob) == prob):
        exito = True
    return exito

def llamarComodin(matR:list, matI:list, prob:int, comodines:list)->bool:
    '''
    Pre: Recibe 2 matrices, un entero y una lista
    Post: En caso de que la funcion "exito", la cual depende de "prob", retorne TRUE, 
    se generara un comodin al azar, el cual se guardara en la lista para ser usado cuando el usuario decida.
    En caso de que el usuario decida usar un comodin, se modificaran las matrices cuando llamamos "comodinSelec" o se seleccionara un turno extra
    dependiendo del comodin elegido.
    Esta funcion siempre retorna FALSE a menos que se use un comodin de "turno extra", 
    en tal caso se retornara TRUE.
    '''
    if (exito(True)):
        opcion = random.randint(1,4)
        if (opcion == 1):
            print("Conseguiste comodin Replay, tienes un turno extra!")
            comodines[0] = comodines[0] + 1
            print("Desea usar un turno extra? actualmente tiene: ", comodines[0])
            if (input("si/no ") == "si"):
                comodines[0] = comodines[0] - 1
                return True
        else:
            comodinSelect(matR, matI, comodines, opcion)
    if (comodines[0] > 0 or comodines[1] > 0 or comodines[2] > 0 or comodines[3] > 0):
        comodinCheck(matR, matI, comodines, opcion)
    return False

def comodinSelect(matR:list, matI:list, comodines:list, opcion:int)->None:
    #Dependiendo del resultado del Randint en la funcion "llamarComodin", la variable "opcion" varia.
    #Segun el numero que sea "opcion" esta llama a otras funciones que modifican el tablero
    if (opcion == 2):
        print("Conseguiste carta Layout, se restribuiran las fichas a tu oponente >.<")
        comodines[1] = comodines[1] + 1
        print("Desea usar un Layout? actualmente tiene: ", comodines[1])
        if (input("si/no ") == "si"):
            comodines[1] = comodines[1] - 1
            cartaLayout(matR)
            cartaLayout(matI)
    elif (opcion == 3):
        print("Conseguiste carta Toti el tablero le refleja a tu oponente")
        comodines[2] = comodines[2] + 1
        print("Desea usar un Toti? actualmente tiene: ", comodines[2])
        if (input("si/no ") == "si"):
            comodines[2] = comodines[2] - 1
            otraOpcion= random.randint(1,2)
            if otraOpcion == 1:
                print("se espejo horizontalmente uwu")
                carTotiH(matR)
                carTotiH(matI)
            elif otraOpcion == 2:
                print("Esta vez se espejo verticalmente uwu")
                carTotiV(matR)
                carTotiV(matI)                   
    else:
        print("Conseguiste comodin Fatality, el tablero se transpone a tu oponente uwu")
        comodines[3] = comodines[3] + 1
        print("Desea usar un Fatality? actualmente tiene: ", comodines[3])
        if (input("si/no ") == "si"):
            comodines[3] = comodines[3] - 1
            fatality(matR)
            fatality(matI)

def comodinCheck(matR:list, matI:list, comodines:list, opcion:int)->None:
    #En el caso de que el jugador tenga un comodin acumulado que quiera usar ingresa en esta funcion
    #Si no quiere usarlo se guarda en la lista "comodines"
    if (comodines[0] >= 1 and opcion != 1):
            print("Desea usar un turno extra? actualmente tiene: ", comodines[0])
            if (input("si/no ") == "si"):
                comodines[0] = comodines[0] - 1
                return True
    if (comodines[1] >= 1 and opcion != 2):
        print("Desea usar un Layout? actualmente tiene: ", comodines[1])
        if (input("si/no ") == "si"):
            comodines[1] = comodines[1] - 1
            cartaLayout(matR)
            cartaLayout(matI)
    if (comodines[2] >= 1 and opcion != 3):
        print("Desea usar un Toti? actualmente tiene: ", comodines[2])
        if (input("si/no ") == "si"):
            comodines[2] = comodines[2] - 1
            otraOpcion= random.randint(1,2)
            if otraOpcion == 1:
                print("se espejo horizontalmente uwu")
                carTotiH(matR)
                carTotiH(matI)
            elif otraOpcion == 2:
                print("Esta vez se espejo verticalmente uwu")
                carTotiV(matR)
                carTotiV(matI)
    if (comodines[3] >= 1 and opcion != 4):
        print("Desea usar un Fatality? actualmente tiene: ", comodines[3])
        if (input("si/no ") == "si"):
            comodines[3] = comodines[3] - 1
            fatality(matR)
            fatality(matI)

def cartaLayout(mat:list)->None:
    #recibe una matriz previamente creada y reordena las casillas en forma aleatoria
    random.shuffle(mat)

def fatality(mat:list)->None:
    #Carta Fatality, recibe una matriz y cambia las filas por columnas, y las columnas por filas
    fila = 0
    for j in range(len(mat)):
        lista = []
        i = fila
        column = j
        while (i < len(mat) and column >= 0):
            lista.append(mat[i][column])
            i += 1
            column -= 1
        i = fila
        column = j
        while (i < len(mat) and column >= 0):
            mat[i][column] = lista[-1]
            column -= 1
            i += 1
            lista.pop()

    col = len(mat) - 1
    for j in range(1, len(mat)):
        lista = []
        i = j
        column = col
        while (i < len(mat) and column >= 0):
            lista.append(mat[i][column])
            i += 1
            column -= 1

        i = j
        column = col
        while (i < len(mat) and column >= 0):
            mat[i][column] = lista[-1]
            i += 1
            column -= 1
            lista.pop()

def carTotiH(mat:list)->None:
    '''
    Pre: recibe una matriz de numeros previamente creado
    Post: retorna una matriz en modo espejo en sus filas
    ''' 
    for i in range(len(mat)):
        fila = []
        for j in range(len(mat[i])):
            fila.append(mat[i][len(mat[i])-1-j])           
        mat[i] = fila

def carTotiV(mat:list)->None:
    '''
    Pre: recibe una matriz de numeros previamente creado
    Post: retorna una matriz en modo espejo en sus columnas
    '''    
    for i in range(len(mat)):
        columna = []
        for j in range(len(mat[i])):
            columna.append(mat[i][len(mat[j])-1-j])      
        mat[i] = (columna)

def impM(mat:list)->None:
    #imprime las coordenadas previamente seleccionadas en una unica matriz que las muestra, mientras
    #las otras coordenadas son incognitas
    print("\n")
    for i in range(len(mat)):
        print(mat[i])
    print("\n")

def nombres(num:int)->str:
    '''
    Pre: recibe un entero valido 
    Post: retorna un str 
    '''
    if (num == 1):
        nombre = input("Ingrese el primer nombre: ")
    else:
        nombre = input("Ingrese el segundo nombre: ")
    return nombre
    
def tiempo()->int:
    '''
    Pre: --
    Post: retorna un numero entero valido que define la duracion y por lo tanto el tamaño
    de las matrices.
    '''
    system("cls")
    duracion = 0
    while (duracion == 0):
        print("Elija una Duracion: ")
        print("1)Corto")
        print("2)Mediano")
        print("3)Largo")
        duracion = int(input())
        if (duracion != 1 and duracion != 2 and duracion != 3):
            duracion = 0
            print("Debe elegir una opcion valida \n")
    system("cls")
    return duracion

def confProb()->int:
    '''
    Pre: -
    Post: retorna un numero entero que representa la probabilidad de los comodines
    '''
    probabilidad = 0
    while (probabilidad == 0):
        print("Por defecto las probabilidades de que le caigan cartas comodin es 1 en 5\n")
        print("Desea cambiar esto? si/no")
        probabilidad = input()
       #system("cls")
        if (probabilidad == "si"):
            probabilidad = input("Ingrese un numero para fijar la probabilidad: ")
            while not probabilidad.isnumeric():
                print("Coloque un Caracter Valido")
                probabilidad = input("Ingrese un numero para fijar la probabilidad: ")
                 #system("cls")
            else:
                print("Ahora la probabilidad es 1 en ",probabilidad)
                input("Presione enter para continuar")
        elif (probabilidad == "no"):
            probabilidad = 5
        else:
            probabilidad = 0
            print("Ingrese una opcion valida")
    return int(probabilidad)

def mostrarRecord(record:list)->None:
    #recibe una lista previamente  creada en la funcion "menu" y llenada en la funcion "inicioGame" 
    #para saber las veces que el jugador gano

    if (record[1] > record[3]):
        print("El jugador: ", record[0], " ha ganado ", record[1], " veces!")
        print("El jugador: ", record[2], " ha ganado ", record[3], " veces!")
    elif (record[1] < record[3]):
        print("El jugador: ", record[2], " ha ganado ", record[3], " veces!")
        print("El jugador: ", record[0], " ha ganado ", record[1], " veces!")
    else:
        print("Ambos jugadores estan empatados con: ", record[1], " victorias!")
    input("Presione enter para salir")
    system("cls")
    
def cerrar ()->None:
    #cierra el programa, se acaba el juego
    fin = input("Nos vemos")
    
def inicioGame(nom1:str, nom2:str, dura:int, prob:int, record:list)->None:
    #Es la funcion que se encarga de contener los datos por defecto o configurados por el usuario en "menu", 
    # para iniciar el juego, llevando la lista del conteo de los ganadores y comodines.
    print("Los parametros que tiene son:\n")
    print("El primer jugador(a) es: ",nom1)
    print("El segundo jugador(a) es: ",nom2)
    print("-La Duracion puede ser 1 = corta, 2 = media, 3 = larga, en su caso la duracion es: ", dura)
    print("-Tiene 1 en ", prob," chances de que le caiga un comodin")
    input("Presione enter para continuar")
    comodinesJ1 = [0,0,0,0]
    comodinesJ2 = [0,0,0,0]
    coin = 0
    coin2 = 0
    if (dura == 1 or dura == 2 or dura == 3):

        matR = generadorM(dura)
        matI = generadorMI(dura)
        matR2 = generadorM(dura)
        matI2 = generadorMI(dura)
        jugadorA = "1"
        jugadorB = "2"
        rangoM = (dura*dura*16)//2
        while (coin != rangoM and coin2 != rangoM):
            coin = turno(matR, matI, matR2, matI2, jugadorA, prob, comodinesJ1, coin)
            if (coin != rangoM and coin2 != rangoM):
                coin2 = turno(matR2, matI2, matR, matI, jugadorB, prob, comodinesJ2, coin2)
        if (coin == rangoM):
            record[1] = record[1] + 1
            if record[1] > 4:
                record[1]=0
        elif (coin2 == rangoM):
            record[3] = record[3] + 1
            if record[3] > 4:
                record[3]=0
    else:
        print("caracter invalido") 

def menu ()->None:
    #esta funcion es la que se encarga de llamar a mis otras funciones y asignarle las variables que 
    #me guardan los valores de estas
    nombre1 = nombres(1)
    nombre2 = nombres(2)
    record = [nombre1, 0, nombre2, 0]
    probabilidad = 5
    duracion = 1
    salir = False
    while not salir:
        system("cls")
        print("Menu de Opciones:" )
        print("1)Comodines")
        print("2)Duracion")
        print("3)Record")
        print("4)Inicio")
        print("0)Salir")
        print("\n")
        op = input("Ingrese una opcion: ")
        if (op == "1"):
            probabilidad = confProb()
        elif (op == "2"):
            duracion = tiempo()
        elif (op == "3"):
            mostrarRecord(record)
        elif (op == "4"):
            inicioGame(nombre1, nombre2, duracion, probabilidad, record)
        elif (op == "0"):
            cerrar()
            salir = True
        else:
            input("Ingrese una opcion valida, presione enter para continuar")

def main ()->None:
    print("Bienvenidos al juego Reglas...Reglas...Emm\n",)
    print("Solo se aceptan 2 jugadores por turno")
    menu()
main()