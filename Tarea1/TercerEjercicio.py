import big_o

def solution(S):
    """
    Funcion que calcula el indice de la cadena que se puede dividir en dos partes
    que son iguales.
    ----------
    Parametros:
    S: str -> Cadena de caracteres
    -------
    Retorna:
    int -> Indice de la cadena
    """
    # Se calcula la longitud de la cadena
    n = len(S)
    # Se recorre la cadena
    for i in range(n):
        # Se verifica si una subcadena de "S" desde el índice inicial hasta el índice "i" es igual a una subcadena de "S" desde el índice "i+1" hasta el final de "S", pero invertida.
        if S[:i] == S[i+1:][::-1]:
            # Se retorna el indice de la cadena
            return i

# Se ejecuta el programa
if __name__ == "__main__":
    # Se pide la cadena
    S = input("Ingrese la cadena: ")
    # Se imprime el indice de la cadena
    print(solution(S))

    #Medir la complejidad de tiempo de la función
    for i in range(0,len(S)):
        # Se crea una lista de elementos 
        lista = lambda a: S[i]
        # Se mide la complejidad de tiempo de la función
        best,others = big_o.big_o(solution,lista)

    # Se imprime la complejidad de tiempo de la función
    print(best)