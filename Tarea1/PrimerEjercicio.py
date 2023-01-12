import big_o

def solucion(A):
    """
    Funcion que encuentra el primer número único en una secuencia dada.
    ----------
    Parámetros:
    A : list
        Lista de elementos

    Retorna:
    -------
    int
        Primer elemento único
    """
    # Recorrer la lista de elementos
    for i in range(len(A)):
        # Si el elemento solo se repite una vez en la lista, se retorna el elemento
        if A.count(A[i]) == 1:
            # Retornar el elemento
            return A[i]
            

# Se ejecuta el programa
if __name__ == "__main__":

    # Se pide la lista de elementos
    A = input("Ingrese la lista de elementos separada por comas: ").split(",")
    # Se imprime el elemento unico
    print(solucion(A))

    #Medir la complejidad de tiempo de la función
    for i in range(0,len(A)):
        # Se crea una lista de elementos 
        lista = lambda a: A[i]
        # Se mide la complejidad de tiempo de la función
        best,others = big_o.big_o(solucion,lista)

    # Se imprime la complejidad de tiempo de la función
    print(best)
