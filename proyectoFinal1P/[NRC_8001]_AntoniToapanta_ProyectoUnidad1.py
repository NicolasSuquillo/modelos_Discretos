"""
El juego de las escondidas es un juego que muchos de nosotros jugabamos de pequeños, acompañados de todos nuestros amigos, contamos con una persona que busca y los demas se esconden. El objetivo principal es concontrar a las demas personas en menor tiempo posible en esta caso se lo hara por turnos, y si encuentra a todos gana el juego

Autores:
Antoni Toapanta Nicolas Suquillo

Verisión:
VER.1.0
"""

import random  # libreria requerida para crear numeros randomicos
# Importamos libreria del sistema para lograr tener pantallas limpias por cada proceso
from os import system
escondites = ["pileta", "casa_del_arbol", "arbusto", "juegos_del_parke", "estatua", "laguna", "cabaña",
              "arbol_norte", "arbol_sur", "arbol_este", "arbol_oeste"]  # Creacion de un arreglo con posibles escondistes
jugadores = []  # Guardaremos el nombre de los jugadores


def mostarEscondites(escondites):
    """
    Funcion para mostrar escondites
    Parametros:
    ----------------
    array de escondites

    Retorna
    ----------------
    no retorna nada
    """
    for i in range(len(escondites)):  # Empieza la itetacion de i en un rango igual a ala longitud de los escondites
        print("{}: {}".format(i, escondites[i]))  # mostramos los escondites


def crearJugadores(numJugadores):
    """
    Funcion para crear un arreglo de jugadores
    Parametros:
    ----------------
    numero de jugadores

    Retorna
    ----------------
    retorna  un arreglo de jugadores
    """
    # creacion de arreglo que se devolvera al finalizar la funcion
    jugadoresArreglo = []
    # Creacion de un buccle  con un rango igual al numero de jugadores
    for i in range(0, numJugadores):
        # agregamos al arreglo los jugadores que participaran en el juego
        jugadoresArreglo.append(
            input("Ingrese el nombre de jugador {}: ".format(i+1)))
    return jugadoresArreglo  # Retormamos el arreglo


def numAleatorio(numJugadores):
    """
    Funcion crear un numero aleatorio
    Parametros:
    ----------------
    numero de jugadores

    Retorna
    ----------------
    retorna un randomico 
    """
    num = random.randint(
        0, numJugadores-1)  # Usamos la funcion randomica para crear numeros aleatorios en un rango de 0 al numero de jugadores
    return num  # retornamos el numero aleatorio


def seEncuentra(lugar, diccionarioJuego, escondidos):
    """
    Funcion para saber si se encuentra el jugador y devolver el numero de personas por encontrar
    Parametros:
    ----------------
    lugar a buscar, lugare donde se encuebran escondidos y numero de personas por busacar

    Retorna
    ----------------
    no retorna en numero de escondidos de encontrar
    """
    # conprobamos si el lugar existe en mi diccionario de juego
    if lugar in diccionarioJuego:
        print("Encontraste a {}".format(diccionarioJuego[lugar]))
        # restamos el numero de personas por encontrar
        escondidos -= 1
    else:
        # retornamos las personas que faltan encontrar
        print("No se encuentra nadie")
    return escondidos


if __name__ == "__main__":

    print("Numero de jugadores minimo 3 y maximo 5")
    # creacion de la coleccion donde se encontrara guaradado el lugar y la persona escondida
    juego = {}
    # validamos el numero de jugadores que pueden participar
    while True:
        # ingresamos el numero de jugadores
        numJugadores = int(input("Ingrese el numero de jugadores: "))
        # comprobamos si existe el numero de jugadores en el rango
        if numJugadores < 3 or numJugadores > 5:
            # Informacion de jugadores fuera de rango
            print("Numeros de jugadores superior/inferior recuerde minimo 3 y maximo 5")
        else:
            break
    # para calcular turnos sumamos el numero de jugadores mas 2
    turnos = numJugadores*2
    # Creamos los jugadores
    jugadores = crearJugadores(numJugadores)
    # Seleccionamos a la persona que buscara
    buscador = jugadores.pop(numAleatorio(numJugadores))
    # el el numero de personas escodidas tomando de la lista de juegadores sin contar al que busca
    escondidos = len(jugadores)
    # funcion para limpiar pantalla
    system("cls")

    # Los demas Jugadores empiezan a buscar donde esconderse

    # mostramos la informacion del juego
    print("Buscador: {}, Jugadores: {}".format(buscador, jugadores))
    # alertar a los demas jugadores
    print("JUGADORES!!! INTENTEN QUE EL BUSCADOR NO VEA DONDE SE ESCONDEN")
    # pausa hasta que presione una tecla
    system("pause")
    # limpia la pantalla
    system("cls")
    # Seleccion de escondite de los jugadores
    for i in range(0, len(jugadores)):
        # Muestra todos los lugares donde se pueden encontrar
        mostarEscondites(escondites)
        # escondites dentro del rango existente
        while True:
            # Guardamos el lugar donde se escondera nuestro jugador
            escondite = int(
                input("{} seleccione un escondite: ".format(jugadores[i])))
            # Comprobamos si exite o no el escondite
            if escondite < 0 or escondite > len(escondites):
                system("cls")
                print("Escondite no existente")
            else:
                juego[escondites[escondite]] = jugadores[i]
                system("cls")
                break
    # limpia la pantalla
    system("cls")

    # Empieza a  buscar a alos demas jugadores
    # si el numero del turnos es diferente de 0 y si las personas escondidas son diferente de 0 salemos de nuestro bucle
    while turnos != 0 and escondidos != 0:
        system("cls")
        # muestra las personas por buscar y las oportunidades que tiene para encontrales
        print("{} empieza a buscar a tus amigos, buen suerte tienes {} oportunidades y tines {} por buscar".format(
            buscador, turnos, escondidos))
        # empeiza a caminar en el parque se pude eleguir entre 4 opciones
        caminar = int(input(
            "Te encuentras en un parque de tu ciudad pudes caminar al \n1.-Norte\n2.-Este\n3.-Sur\n4.-Oeste\nSeleccione:"))
        system("cls")
        # Camina Hacia el norte del parque
        if caminar == 1:
            # informacion donde nos encontramos ubicados
            print("NORTE")
            # si selecciona alguna de las opciones y si no se encuetra pierde 1 turno
            buscarN = int(input(
                "Seleccione donde quiere buscar:\n1.-Arbol norte\n2.-Arbusto\n3.-Estatua\n0.-Regresar Al Parque\nSeleccione:"))
            # si selecciona la opcion de arbol norte
            if buscarN == 1:
                # comprueba si existe alguien ahi
                escondidos = seEncuentra("arbol_norte", juego, escondidos)
                # se resta un turno
                turnos -= 1  
            # si selecciona la opcion de arbusto
            elif buscarN == 2:  
                # comprueba si existe alguien ahi
                escondidos = seEncuentra("arbusto", juego, escondidos)
                 # se resta un turno
                turnos -= 1 
             # si selecciona la opcion de estatua
            elif buscarN == 3: 
                # comprueba si existe alguien ahi
                escondidos = seEncuentra("estatua", juego, escondidos)
                # se resta un turno
                turnos -= 1  
             # si desea regresar al parque
            elif buscarN == 0: 
                 # regresa al parque principal
                print("Regresando Al Parque") 
         # Camina Hacia el Este del parque
        elif caminar == 2: 
            # informacion donde nos encontramos ubicados
            print("ESTE")  
            # si selecciona alguna de las opciones y si no se encuetra pierde 1 turno
            buscarE = int(input(
                "Seleccione donde quiere buscar:\n1.-Arbol este\n2.-Pileta\n3.-Casa del Arbol\n0.-Regresar Al Parque\nSeleccione:"))
             # si selecciona la opcion arbol este
            if buscarE == 1: 
                # comprueba si existe alguien ahi
                escondidos = seEncuentra("arbol_este", juego, escondidos)
                # se resta un turno
                turnos -= 1  
            # si selecciona la opcion pileta
            elif buscarE == 2:  
                # comprueba si existe alguien ahi
                escondidos = seEncuentra("pileta", juego, escondidos)
                # se resta un turno
                turnos -= 1  
             # si selecciona la opcion casa del arbol
            elif buscarE == 3: 
                # comprueba si existe alguien ahi
                escondidos = seEncuentra("casa_del_arbol", juego, escondidos)
                 # se resta un turno
                turnos -= 1 
            # si desea regresar al parque
            elif buscarE == 0:  
                 # regresa al parque principal
                print("Regresando Al Parque") 
        # Camina Hacia el Sur del parque
        elif caminar == 3:  
            # informacion donde nos encontramos ubicados
            print("SUR")  
            # si selecciona alguna de las opciones y si no se encuetra pierde 1 turno
            buscarS = int(input(
                "Seleccione donde quiere buscar:\n1.-Arbol sur\n2.-Juegos del parque sur\n3.-Cabaña\n0.-Regresar Al Parque\nSeleccione:"))
            # si selecciona la opcion arbol sur
            if buscarS == 1:  
                # comprueba si existe alguien ahi
                escondidos = seEncuentra("arbol_sur", juego, escondidos)
                # se resta un turno
                turnos -= 1  
             # si selecciona la opcion juegos del parque
            elif buscarS == 2: 
                # comprueba si existe alguien ahi
                escondidos = seEncuentra("juegos_del_parke", juego, escondidos)
                # se resta un turno
                turnos -= 1  
            # si selecciona la opcion cabaña
            elif buscarS == 3:  
                # comprueba si existe alguien ahi
                escondidos = seEncuentra("cabaña", juego, escondidos)
                 # se resta un turno
                turnos -= 1 
            # si desea regresar al parque
            elif buscarS == 0:  
                 # regresa al parque principal
                print("Regresando Al Parque") 
        # Camina Hacia el Oeste del parque
        elif caminar == 4:  
            #informacion donde nos encontramos ubicados
            ("OESTE")  
            #si selecciona alguna de las opciones y si no se encuetra pierde 1 turno
            buscarO = int(input(
                "Seleccione donde quiere buscar:\n1.-Arbol oeste\n2.-Laguna\n0.-Regresar Al Parque\nSeleccione:"))
             # si selecciona la opcion arbol oeste
            if buscarO == 1: 
                # comprueba si existe alguien ahi
                escondidos = seEncuentra("arbol_oeste", juego, escondidos)
                 # se resta un turno
                turnos -= 1 
             # si selecciona la opcion laguna
            elif buscarO == 2: 
                # comprueba si existe alguien ahi
                escondidos = seEncuentra("laguna", juego, escondidos)
                # se resta un turno
                turnos -= 1  
            # si desea regresar al parque
            elif buscarO == 0:  
                 # regresamos al parque principal
                print("Regresando Al Parque") 
        system("pause")
         # si el jugador principal encontro a todos el numero de escodidos sera 0 y ganara el juego
        if (escondidos == 0): 
            # informacion de que gano la partida
            print("Ganaste!!! eres un Capo :)")
         # si no encuentra a todas las personas y su turno son 0 pierde
        else: 
            # informacion que dice que perdio el game
            print("Perdiste :c ")  
