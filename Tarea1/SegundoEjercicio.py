
from datetime import datetime
import big_o

def solution(E:str, L:str)-> int:
    """
    Funcion que calcula el costo de estacionamiento
    ----------
    Parametros:
    
    E: str -> Hora de entrada
    L: str -> Hora de salida
    ----------
    Retorna: 
    int -> Costo de estacionamiento
    """

    #En tiempo_e se guarda la hora de entrada en formato datetime
    tiempo_e = datetime.strptime(E, "%H:%M")
    #En tiempo_l se guarda la hora de salida en formato datetime
    tiempo_l = datetime.strptime(L, "%H:%M")

    #Se calcula la diferencia entre la hora de entrada y la hora de salida
    diff_minutos = int((tiempo_l - tiempo_e).total_seconds() / 60)

    #Se calcula el costo de estacionamiento
    horas_completas = diff_minutos // 60
    #Se calcula el costo de estacionamiento
    horas_incompletas = diff_minutos % 60

    #Si las horas completas son mayores a 0, se calcula el costo de estacionamiento
    if horas_completas > 0:
        #En costo se guarda el costo de estacionamiento
        costo = 2 + 3 + (horas_completas - 1) * 4 
    #Si las horas completas son 0, se calcula el costo de estacionamiento
    else:
        #En costo se guarda el costo de estacionamiento
        costo = 0
    #Si las horas incompletas son mayores a 0, se calcula el costo de estacionamiento
    if horas_incompletas > 0:
        #Se calcula el costo de estacionamiento
        costo += 4
    #Se retorna el costo de estacionamiento
    return costo

#Funcion para validar que el usuario ingrese una hora
def validar_hora(hora):
    """
    Funcion que valida que el usuario ingrese una hora valida
    ----------
    Parametros:

    hora: str -> Hora ingresada por el usuario
    ----------
    Retorna:
    bool -> True si la hora es valida, False si la hora no es valida
    """
    #Se utiliza try y except para validar que el usuario ingrese una hora valida
    try:
        #Se utiliza datetime.strptime para validar que el usuario ingrese una hora valida
        datetime.strptime(hora, '%H:%M')
        #Se retorna True si la hora es valida
        return True
        #Se retorna False si la hora no es valida
    except ValueError:
        return False


#Funcion principal
if __name__ == "__main__":

    # Solicitamos al usuario que ingrese la hora de entrada
    E = input("Ingrese la hora de entrada (HH:MM): ")
    #Validamos que el usuario ingrese una hora valida
    while not validar_hora(E):
        E = input("Ingrese una hora valida (HH:MM): ")
    # Solicitamos al usuario que ingrese la hora de salida
    L = input("Ingrese la hora de salida (HH:MM): ")
    #Validamos que el usuario ingrese una hora valida
    while not validar_hora(L):
        L = input("Ingrese una hora valida (HH:MM): ")

    # Imprimimos el resultado
    print(solution(E, L))
