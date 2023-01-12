import big_o

def solution(N):
    """
    Funcion que calcula el exponente de 2 mas grande de un numero
    ----------
    Parametros:
    N: int -> Numero entero

    ----------
    Retorna:
    int -> Exponente de 2 mas grande
    
    """
    # Se calcula el exponente de 2 mas grande
    # Se inicializa el exponente en 0
    k = 0
    # Se comprueba que N sea divisible entre 2
    while N % 2**(k+1) == 0:
        # Se suma 1 al exponente
        k += 1
    # Se retorna el exponente
    return k
    
#Se ejecuta el programa
if __name__ == "__main__":

    # Se pide el numero
    N = int(input("Ingrese el numero: "))
    #Se imprime la solucion
    print(solution(N))

    # Se crea una lista de elementos 
    lista = lambda a: N
    # Se mide la complejidad de tiempo de la función
    best,others = big_o.big_o(solution,lista)

    # Se imprime la complejidad de tiempo de la función
    print(best)