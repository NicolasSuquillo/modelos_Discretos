import big_o

def generar_cadena(A: int, B: int) -> str:
    """
    Funcion que genera una cadena de caracteres a partir de la cantidad de a's y b's
    ----------
    Parametros:
    A: int -> Cantidad de a's
    B: int -> Cantidad de b's
    ----------
    Retorna: 
    str -> Cadena de caracteres
    """
    #Se guarda el resultado en una variable
    resultado = ""
    #Se comprueba que A y B sean mayores a 0
    while A > 0 or B > 0:
        #Se comprueba que el resultado tenga al menos 2 caracteres
        if len(resultado) >= 2 and resultado[-1] == resultado[-2]:
            #Se comprueba que el ultimo caracter sea a
            if resultado[-1] == 'a':
                #Se comprueba que B sea mayor a 0
                if B > 0:
                    #Se agrega un b al resultado
                    resultado += 'b'
                    # Se resta 1 a B
                    B -= 1
                #Se comprueba que A sea mayor a 0
                else:
                    #Se agrega un a al resultado
                    resultado += 'a'
                    #Se resta 1 a A
                    A -= 1
            #Se comprueba que el ultimo caracter sea b
            else:
                #Se comprueba que A sea mayor a 0
                if A > 0:
                    #Se agrega un a al resultado
                    resultado += 'a'
                    #Se resta 1 a A
                    A -= 1
                #Se comprueba que B sea mayor a 0
                else:
                    #Se agrega un b al resultado
                    resultado += 'b'
                    #Se resta 1 a B
                    B -= 1
        #Se comprueba que A sea mayor a B
        elif A > B:
            #Se agrega un a al resultado
            resultado += 'a'
            #Se resta 1 a A
            A -= 1
        #Se comprueba que B sea mayor a A
        else:
            #Se agrega un b al resultado
            resultado += 'b'
            #Se resta 1 a B
            B -= 1
    #Se retorna el resultado    
    return resultado

#Se ejecuta el programa
if __name__ == "__main__":
    
    #Solicitamos los datos de A al usuario
    A = int(input("Ingrese el numero de a's: "))
    #Solicitamos los datos de B al usuario
    B = int(input("Ingrese el numero de b's: "))
    
    #Imprimimos el resultado
    print(generar_cadena(A, B))
