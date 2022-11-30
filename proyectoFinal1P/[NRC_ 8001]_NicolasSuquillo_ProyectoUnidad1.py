from gtts import gTTS
from os import system, name
from time import sleep 

#Juego del telefono descompuesto
system("cls")
print("\t\t\t\t\t-----------------------------------------------")
print("\t\t\t\t\t|Bienvenido al juego del telefono descompuesto|")
print("\t\t\t\t\t-----------------------------------------------\n")
print("\t\t\tReglas-----------------------------------------------------------------")
print("\t\t\t|                                                                       |")
print("\t\t\t|El juego consiste en que se te mostrara una frase y deberas adivinarla |")
print("\t\t\t|La frase se mostrara durante un tiempo y luego desaparecera            |")
print("\t\t\t|Posteriormente se tendra que ingresar la frase que se cree es          |")
print("\t\t\t|                                                                       |")
print("\t\t\t-----------------------------------------------------------------------\n")
print("\t\t\t---------------------------------")
print("\t\t\t|Si aciertas ganas, si no pierdes|")
print("\t\t\t---------------------------------\n")
print("\t\t\tBuena suerte!!!!\n\n\n\n\n")
system("pause")
system("cls")

#Se leen las frases de un txt y se guardan en una lista
def guardarFrases():
    """
    Es un proceso que guarda las frases que se encuentran en archivo txt en una lista
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        frases: lista
            Lista que contiene las frases del archivo txt
    """
    #guarda las frases en una lista
    frases = []
    #Se abre el archivo
    archivo = open("frases.txt", "r")
    #Se lee el archivo
    with open("frases.txt", "r") as archivo:
        #Se guarda cada linea en una lista
        for linea in archivo:
            #Se guarda la linea en la lista, se le quita el salto de linea y espacios
            frases.append(linea.lower().strip())
    #Se cierra el archivo
    archivo.close()
    #Se regresa la lista
    return frases

#El usuario ingresa un numero y se le asigna una frase
def elegirFrase(frases):
    """
    Es un proceso que se encarga de elegir una frase de la lista de frases, 
    posteriormente de haber pedido al usuario que ingrese un numero
    Parametros:
    ------------
        frases: lista
            Lista que contiene las frases del archivo txt
    
    Retorna:
    ------------
        frase: str
            Frase que se eligio de la lista de frases
    """
    #Se le pide al usuario que ingrese un numero
    frase = ""
    #Se valida que el numero este en el rango de la lista
    while frase == "":
        #Se le pide al usuario que ingrese un numero
        numero = input("Ingresa un numero del 1 al 20: ")
        #Se valida que el numero este en el rango de la lista
        if numero == "1":
            #Se guarda la frase en la variable
            frase = frases[0]
        #Se valida que el numero este en el rango de la lista    
        elif numero == "2":
            #Se guarda la frase en la variable
            frase = frases[1]
        #Se valida que el numero este en el rango de la lista
        elif numero == "3":
            #Se guarda la frase en la variable
            frase = frases[2]
        #Se valida que el numero este en el rango de la lista
        elif numero == "4":
            #Se guarda la frase en la variable
            frase = frases[3]
        #Se valida que el numero este en el rango de la lista
        elif numero == "5":
            #Se guarda la frase en la variable
            frase = frases[4]
        #Se valida que el numero este en el rango de la lista
        elif numero == "6":
            #Se guarda la frase en la variable
            frase = frases[5]
        #Se valida que el numero este en el rango de la lista
        elif numero == "7":
            #Se guarda la frase en la variable
            frase = frases[6]
        #Se valida que el numero este en el rango de la lista
        elif numero == "8":
            #Se guarda la frase en la variable
            frase = frases[7]
        #Se valida que el numero este en el rango de la lista
        elif numero == "9":
            #Se guarda la frase en la variable
            frase = frases[8]
        #Se valida que el numero este en el rango de la lista
        elif numero == "10":
            #Se guarda la frase en la variable
            frase = frases[9]
        #Se valida que el numero este en el rango de la lista
        elif numero == "11":
            #Se guarda la frase en la variable
            frase = frases[10]
        #Se valida que el numero este en el rango de la lista
        elif numero == "12":
            #Se guarda la frase en la variable
            frase = frases[11]
        #Se valida que el numero este en el rango de la lista
        elif numero == "13":
            #Se guarda la frase en la variable
            frase = frases[12]
        #Se valida que el numero este en el rango de la lista
        elif numero == "14":
            #Se guarda la frase en la variable
            frase = frases[13]
        #Se valida que el numero este en el rango de la lista
        elif numero == "15":
            #Se guarda la frase en la variable
            frase = frases[14]
        #Se valida que el numero este en el rango de la lista
        elif numero == "16":
            #Se guarda la frase en la variable
            frase = frases[15]
        #Se valida que el numero este en el rango de la lista
        elif numero == "17":
            #Se guarda la frase en la variable
            frase = frases[16]
        #Se valida que el numero este en el rango de la lista
        elif numero == "18":
            #Se guarda la frase en la variable
            frase = frases[17]
        #Se valida que el numero este en el rango de la lista
        elif numero == "19":
            #Se guarda la frase en la variable
            frase = frases[18]
        #Se valida que el numero este en el rango de la lista
        elif numero == "20":
            #Se guarda la frase en la variable
            frase = frases[19]
        #Si el numero no esta en el rango
        else:
            #Se le indica al usuario que ingrese un numero valido
            print("Numero invalido")
    #Se regresa la frase
    return frase

#Se limpia la pantalla
def limpiar():
    """
    Es un proceso que se encarga de limpiar la pantalla
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No tiene parametros de salida
    """
    # for windows 
    if name == 'nt': 
        #Se limpia la pantalla
        _ = system('cls')

#Mostrar por un tiempo la frase elegida
def mostrarFrase(frase):
    """
    Es un proceso que se encarga de mostrar la frase elegida por el usuario durante unos segundos
    Parametros:
    ------------
        frase: str
            Frase que se eligio de la lista de frases
    
    Retorna:
    ------------
       No tiene parametros de salida
    """
    #Se imprime la frase
    print(frase)
    #Se espera 0.6 segundos
    sleep(0.6)
    #Se limpia la pantalla
    limpiar()

#Se convierte la frase a audio
def frase_a_audio(frase):
    """
    Es un proceso que se encarga de convertir la frase elegida por el usuario a un archivo de audio .mp3 y lo guarda en la carpeta del proyecto
    para poder reproducirlo
    Parametros:
    ------------
        frase: str
            Frase que se eligio de la lista de frases
    
    Retorna:
    ------------
       No tiene parametros de salida
    """
#Guarda la frase en un archivo de audio
    audio = gTTS(frase, lang='es')
#Se guarda el audio
    audio.save("frase.mp3")
#Se reproduce el audio
    system("frase.mp3")

#Se adivina la frase
def adivinarFrase(frase):
    """
    Es un proceso que se encarga de ver si la frase que ingreso el usuario es igual a la frase que se eligio de la lista de frases
    Parametros:
    ------------
        frase: str
            Frase que se eligio de la lista de frases
    
    Retorna:
    ------------
       No tiene parametros de salida
    """
    #Se imprime adivina la frase
    print("Adivina la frase")
    #Se limpia la pantalla
    limpiar()
    #Se muestra la frase
    mostrarFrase(frase)
    #Se limpia la pantalla
    limpiar()
    #Se le pide al usuario que adivine la frase
    adivinanza = input("Ingresa la frase que crees que es: ")
    #Se compara la frase con la adivinanza
    if adivinanza.lower().strip() == frase:
        #Se imprime que la adivinanza es correcta
        print("Felicidades, ganaste\n")
    else:
        #Se imprime que la adivinanza es incorrecta
        print("Perdiste\n")
    #Se pausa hasta que el usuario presione una tecla
    system("pause")
    #Se limpia la pantalla
    limpiar()
    

#Se ejecuta el juego
def main():
    """
    Es un proceso que se encarga de correr el juego
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
       No tiene parametros de salida
    """
    #Se guarda las frases en la variable
    frases = guardarFrases()
    #Se guarda la frase elegida en la variable
    frase = elegirFrase(frases)
    #Se envia la frase para que el usuario la adivine
    adivinarFrase(frase)
    #Se muestra cual era la frase
    print("La frase era: ", frase)
    #Se convierte la frase a audio
    frase_a_audio(frase)
    #Se finaliza el programa
    print("Gracias por jugar\n\n")
    #Se pausa hasta que el usuario presione una tecla
    system("pause")
    
#Se ejecuta el programa
main()