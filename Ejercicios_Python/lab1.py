import sys
import math
import os

def Ejercicio_4():
    """
    Funcion que calcula la arista lateral de una pirámide
    ----------
    """

    # Solicitamos al usuario que ingrese los valores de la altura de la pirámide 
    altura = float(input("Ingresa la altura de la pirámide: "))
    # Solicitamos al usuario que ingrese los valores de la base de la pirámide
    lado_base = float(input("Ingresa el lado de la base de la pirámide: "))

    # Calculamos la arista lateral de la pirámide utilizando la fórmula de la arista lateral
    arista_lateral = math.sqrt((altura ** 2) + ((lado_base / 2) ** 2))

    # Mostramos el resultado al usuario con dos decimales
    print("La arista lateral de la pirámide es: {:.2f}".format(arista_lateral))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def area_trapezoide(base_mayor, base_menor, altura):
    """
    Funcion que calcula el área de un trapecio
    ----------
        base_mayor: float
            Valor de la base mayor del trapecio
        base_menor: float
            Valor de la base menor del trapecio
        altura: float
            Valor de la altura del trapecio

    Retorna:
    ------------
        area: float
            Valor del área del trapecio
    """

    # Calculamos la mediana del trapecio
    mediana = (base_mayor + base_menor) / 2
    # Calculamos el área del trapecio
    return mediana * altura

def Ejercicio_6():
    """
    Funcion que calcula el área de un trapecio
    ----------
    """

    # Solicitamos al uruario el valor de la base mayor del trapecio
    base_mayor = float(input("Ingresa el valor de la base mayor del trapecio: "))
    # Solicitamos al uruario el valor de la base menor del trapecio
    base_menor = float(input("Ingresa el valor de la base menor del trapecio: "))
    # Solicitamos al uruario el valor de la altura del trapecio
    altura = float(input("Ingresa el valor de la altura del trapecio: "))
    # Calculamos el área del trapecio
    area = area_trapezoide(base_mayor, base_menor, altura)
    # Mostramos el resultado al usuario con dos decimales
    print("El área del trapezoide es: {:.2f} m^2".format(area))  
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def Ejercicio_7():
    """
    Funcion que calcula el área de un cilindro
    ----------
    """

    # Solicitamos al usuario que ingrese el radio y la altura del cilindro
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))

    # Calculamos el área del cilindro utilizando la fórmula mencionada anteriormente
    area = 2 * math.pi * radio * altura + 2 * math.pi * radio**2

    # Mostramos el resultado al usuario con dos decimales
    print("El área del cilindro es: {:.2f}".format(area))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def Ejercicio_8():
    """
    Funcion que calcula el área de un círculo
    ----------
    """
    # Pedir al usuario que ingrese el radio del círculo
    radio = float(input("Ingrese el radio del círculo: "))
    # Calcular el área del círculo
    area = math.pi * radio**2
    # Mostrar el resultado al usuario con dos decimales
    print("El área del círculo es: {:.2f}".format(area))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def Ejercicio_9():
    """
    Funcion que calcula el teorema de pitágoras
    ----------
    """
    # Pedimos al usuario que ingrese los valores de los catetos
    a = float(input("Ingrese el valor del primer cateto: "))
    # Pedimos al usuario que ingrese los valores de los catetos
    b = float(input("Ingrese el valor del segundo cateto: "))

    # Calculamos la hipotenusa
    c = (a**2 + b**2)**0.5

    # Imprimimos el resultado
    print("La hipotenusa mide:", c)
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def Ejercicio_11():
    """
    Funcion que convierte de libras a kilos y gramos
    ----------
    """

    # Pedimos al usuario que ingrese el número de libras a convertir
    libras = float(input("Ingresa el número de libras: "))

    # Convertimos las libras a kilos
    kilos = libras * 0.453592
    # Convertimos las libras a gramos
    gramos = libras * 453.592

    # Mostramos el resultado
    print(f"{libras} libras son {kilos} kilos")
    # Mostramos el resultado
    print(f"{libras} libras son {gramos} gramos")
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass 

def Ejercicio_13():
    """
    Funcion para dar la bienvenida al usuario
    ----------
    """

    # Mensaje de bienvenida al usuario
    print("Bienvenido al programa de saludo!")

    # Pedir al usuario que ingrese su nombre
    nombre = input("Por favor, ingrese su nombre: ")

    # Mostrar mensaje de saludo al usuario
    print("Hola, " + nombre + "! ¡Es un placer saludarte!")
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def Ejercicio_14():
    """
    Ingresar un valor en dólares y transformar en euros y yen
    ----------
    """

    # Obtener el tipo de cambio entre dólares y euros y entre dólares y yenes
    dolares_euros = 0.85
    dolares_yen = 105.34

    # Pedir al usuario que ingrese el valor en dólares a convertir
    dolares = float(input("Ingresa el valor en dólares: "))

    # Calcular el equivalente en euros y yenes
    euros = dolares * dolares_euros
    yen = dolares * dolares_yen

    # Mostrar al usuario el resultado de la conversión
    print(f"{dolares} dólares son {euros} euros y {yen} yenes.")
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def Ejercicio_18():
    """
    Ingresar dos números y realizar todas las operaciones aritméticas.
    ----------
    """

    # Solicitamos al usuario que ingrese dos números
    num1 = input("Ingresa un número: ")
    num2 = input("Ingresa otro número: ")

    # Convertimos los números a enteros
    num1 = int(num1)
    num2 = int(num2)

    # Realizamos las operaciones aritméticas
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2

    # Imprimimos los resultados
    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicación:", multiplicacion)
    print("División:", division)
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def encontrar_perímetro(longitud, ancho):
    """
    Función que calcula el perímetro de un rectángulo
    ----------
    Parámetros:
    longitud: float
        Longitud del rectángulo
    ancho: float
        Ancho del rectángulo
    ----------
    Retorna:
    perímetro: float    
        Perímetro del rectángulo
    """
    # Calculamos el perímetro
    perímetro = 2 * (longitud + ancho)
    # Retornamos el perímetro
    return perímetro

def Ejercicio_19():
    """
    Ingresar la longitud y el ancho de un rectángulo y calcular su perímetro.
    ----------
    """

    #Solicitamos al usuario que ingrese la longitud
    longitud = float(input("Ingresa la longitud: "))
    #Solicitamos al usuario que ingrese el ancho
    ancho = float(input("Ingresa el ancho: "))
    #Imprimimos el resultado
    print("El perímetro es:", encontrar_perímetro(longitud, ancho))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def Ejercicio_20():
    """
    Ingresar la longitud en centímetros y convertirla en metro y kilómetro.
    ----------
    """

    # Pide al usuario que ingrese la longitud en centímetros
    centimetros = input("Ingresa la longitud en centímetros: ")

    # Convierte la entrada del usuario a un número (en este caso, un número flotante)
    centimetros = float(centimetros)

    # Divide la longitud en centímetros por 100 para convertirla a metros
    metros = centimetros / 100

    # Divide la longitud en metros por 1000 para convertirla a kilómetros
    kilometros = metros / 1000

    # Muestra al usuario el resultado de la conversión
    print(f"{centimetros} centímetros es igual a {metros:.2f} metros o {kilometros:.6f} kilómetros.")
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def convert_temperature(temp, temp_sc):
    """
    Función que convierte una temperatura de Celsius a Fahrenheit o viceversa
    ----------
    Parámetros:
    temp: float
        Temperatura a convertir
    temp_sc: str
        Escala de temperatura a convertir
    ----------
    Retorna:
    fahrenheit: float
        Temperatura convertida a Fahrenheit
    celsius: float
        Temperatura convertida a Celsius
    """
    # Si la escala de temperatura es Celsius, convertimos a Fahrenheit
    if temp_sc == "C":
        # Formula para convertir de Celsius a Fahrenheit
        fahrenheit = temp * 9/5 + 32
        # Retornamos el resultado
        return fahrenheit
    # Si la escala de temperatura es Fahrenheit, convertimos a Celsius
    elif temp_sc == "F":
        # Formula para convertir de Fahrenheit a Celsius
        celsius = (temp - 32) * 5/9
        # Retornamos el resultado
        return celsius

def Ejercicio_21():
    """
    Ingresar una temperatura en grados Celsius y convertirla a grados Fahrenheit.
    ----------
    """
    # Solicitamos al usuario que ingrese la temperatura en grados Celsius
    temp = float(input("Ingresa la temperatura en grados Celsius: "))
    # Imprimimos el resultado
    print("La temperatura en grados Fahrenheit es:", convert_temperature(temp, "C"))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def Ejercicio_22():
    """
    Calcular la formula de la velocidad
    ----------
    """

    # Pedimos al usuario que introduzca la distancia recorrida y el tiempo
    distancia = float(input("Introduce la distancia recorrida (en km): "))
    tiempo = float(input("Introduce el tiempo transcurrido (en horas): "))

    # Calculamos la velocidad
    velocidad = distancia / tiempo

    # Mostramos el resultado al usuario
    print("La velocidad media es de", velocidad, "km/h")
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def potencia(base, exponente):
    """
    Función que calcula la potencia de un número
    ----------
    Parámetros:
    base: int
        Base de la potencia
    exponente: int
        Exponente de la potencia
    ----------
    Retorna:
    resultado: int
        Resultado de la potencia
    """
    # Inicializamos el resultado
    resultado = 1
    # Iteramos el exponente
    for i in range(exponente):
        # Multiplicamos el resultado por la base
        resultado *= base
    # Retornamos el resultado
    return resultado

def Ejercicio_24():
    """
    Calcular la potencia de un número
    ----------
    """
    # Pedimos al usuario que introduzca la base y el exponente
    base = int(input("Introduce la base: "))
    exponente = int(input("Introduce el exponente: "))
    # Imprimimos el resultado
    print("El resultado es:", potencia(base, exponente))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def calc_raiz(numero):
    """
    Función que calcula la raíz cuadrada de un número
    ----------
    Parámetros:
    numero: int
        Número del que se calculará la raíz cuadrada
    ----------
    Retorna:
    result: float
        Raíz cuadrada del número
    """
    # Intentamos calcular la raíz cuadrada
    try:
        # Calculamos la raíz cuadrada
        result = math.sqrt(numero)
    # Si el número es negativo, mostramos un mensaje de error
    except ValueError:
        # Mostramos un mensaje de error
        print("No se puede calcular la raíz cuadrada de un número negativo")
        # Inicializamos el resultado
        result = None
    # Retornamos el resultado
    return result

def Ejercicio_25():
    """
    Calcular la raíz cuadrada de un número
    ----------
    """
    # Pedimos al usuario que introduzca un número
    numero = int(input("Introduce un número: "))
    # Imprimimos el resultado
    print("La raíz cuadrada de", numero, "es", calc_raiz(numero))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def area_triangulo(base, altura):
    """
    Función que calcula el área de un triángulo
    ----------
    Parámetros:
    base: int
        Base del triángulo
    altura: int
        Altura del triángulo
    ----------
    Retorna:
    area: float
        Área del triángulo
    """
    # Calculamos el área
    area = (base * altura) / 2
    # Retornamos el área
    return area

def Ejercicio_27():
    """
    Calcular el área de un triángulo
    ----------
    """
    # Pedimos al usuario que introduzca la base y la altura
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    # Imprimimos el resultado
    print("El área del triángulo es", area_triangulo(base, altura))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def calcular_area_paralelogramo(base, altura):
    """
    Función que calcula el área de un paralelogramo
    ----------
    Parámetros:
    base: int
        Base del paralelogramo
    altura: int
        Altura del paralelogramo
    ----------
    Retorna:
    area: float
        Área del paralelogramo
    """
    # Calculamos el área
    area = base * altura
    # Retornamos el área
    return area

def Ejercicio_33():
    """
    Calcular el área de un paralelogramo
    ----------
    """
    # Pedimos al usuario que introduzca la base y la altura
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    # Imprimimos el resultado
    print("El área del paralelogramo es", calcular_area_paralelogramo(base, altura))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def Ejercicio_34():
    """
    Calcular la ecuación de la recta. 
    ----------
    """

    # Pedir al usuario que ingrese los valores de x1, y1, x2, y2
    x1 = float(input("Ingresa el valor de x1: "))
    y1 = float(input("Ingresa el valor de y1: "))
    x2 = float(input("Ingresa el valor de x2: "))
    y2 = float(input("Ingresa el valor de y2: "))

    # Calcular la pendiente m
    m = (y2 - y1) / (x2 - x1)

    # Calcular el término independiente b
    b = y1 - m * x1

    # Escribir la ecuación de la recta en la forma "y = mx + b"
    print("La ecuación de la recta es: y = {:.2f}x + {:.2f}".format(m, b))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass


def volumen_esfera(radio):
    """
    Función que calcula el volumen de una esfera
    ----------
    Parámetros:
    radio: int
        Radio de la esfera
    ----------
    Retorna:
    volumen: float
        Volumen de la esfera
    """
    # Calculamos el volumen
    volumen = (4/3) * math.pi * radio**3
    # Retornamos el volumen
    return volumen

def Ejercicio_37():
    """
    Calcular el volumen de una esfera
    ----------
    """
    # Pedimos al usuario que introduzca el radio
    radio = float(input("Introduce el radio: "))
    # Imprimimos el resultado
    print("El volumen de la esfera es", volumen_esfera(radio))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def densidad(masa, volumen):
    """
    Función que calcula la densidad de un objeto
    ----------
    Parámetros:
    masa: int
        Masa del objeto
    volumen: int
        Volumen del objeto
    ----------
    Retorna:
    densidad: float
        Densidad del objeto
    """
    # Calculamos la densidad
    densidad = masa / volumen
    # Retornamos la densidad
    return densidad

def Ejercicio_38():
    """
    Calcular la densidad de un objeto
    ----------
    """
    # Pedimos al usuario que introduzca la masa y el volumen
    masa = float(input("Introduce la masa: "))
    volumen = float(input("Introduce el volumen: "))
    # Imprimimos el resultado
    print("La densidad del objeto es", densidad(masa, volumen))
    # Pedimos al usuario que presione una tecla para continuar
    print("Presione una tecla para continuar...")
    # Se espera a que el usuario presione una tecla
    input()
    # Limpiamos la pantalla
    os.system("cls")
    pass

def salir():
    """
    Funcion que sale del programa
    ----------
    """
    # Salimos del programa
    print("Saliendo del programa...")
    # Salimos del programa
    sys.exit()
    
# Diccionario que contiene las opciones del menú
opciones = {
    # llamamos a la función Ejercicio_4
    "1": Ejercicio_4,
    # llamamos a la función Ejercicio_6
    "2": Ejercicio_6,
    # llamamos a la función Ejercicio_7
    "3": Ejercicio_7,
    # llamamos a la función Ejercicio_8
    "4": Ejercicio_8,
    # llamamos a la función Ejercicio_9
    "5": Ejercicio_9,
    # llamamos a la función Ejercicio_11
    "6": Ejercicio_11,
    # llamamos a la función Ejercicio_13
    "7": Ejercicio_13,
    # llamamos a la función Ejercicio_14
    "8": Ejercicio_14,
    # llamamos a la función Ejercicio_18
    "9": Ejercicio_18,
    # llamamos a la función Ejercicio_19
    "10": Ejercicio_19,
    # llamamos a la función Ejercicio_20
    "11": Ejercicio_20,
    # llamamos a la función Ejercicio_21
    "12": Ejercicio_21,
    # llamamos a la función Ejercicio_22
    "13": Ejercicio_22,
    # llamamos a la función Ejercicio_24
    "14": Ejercicio_24,
    # llamamos a la funcion Ejercicio_25
    "15": Ejercicio_25,
    # llamamos a la funcion Ejercicio_27
    "16": Ejercicio_27,
    # llamamos a la funcion Ejercicio_33
    "17": Ejercicio_33,
    # llamamos a la funcion Ejercicio_34
    "18": Ejercicio_34,
    # llamamos a la funcion Ejercicio_37
    "19": Ejercicio_37,
    # llamamos a la funcion Ejercicio_38
    "20": Ejercicio_38,
    # llamamos a la función salir
    "21": salir
}

# Función principal
if __name__ == "__main__":

    # Ciclo infinito
    while True:
        # Mostramos el menú al usuario
        print("""
        1. Ejercicio 4
        2. Ejercicio 6
        3. Ejercicio 7
        4. Ejercicio 8
        5. Ejercicio 9
        6. Ejercicio 11
        7. Ejercicio 13
        8. Ejercicio 14
        9. Ejercicio 18
        10. Ejercicio 19
        11. Ejercicio 20
        12. Ejercicio 21
        13. Ejercicio 22
        14. Ejercicio 24
        15. Ejercicio 25
        16. Ejercicio 27
        17. Ejercicio 33
        18. Ejercicio 34
        19. Ejercicio 37
        20. Ejercicio 38
        21. Salir
        """)
        # Solicitamos al usuario que ingrese su elección
        eleccion = input("Ingresa tu elección: ")
        
        # Verificamos si la elección es válida
        if eleccion in opciones:
            # Llamamos a la función que corresponde a la elección del usuario
            opciones[eleccion]()
        else:
            # Mostramos un mensaje de error en caso de que la elección sea inválida
            print("Elección inválida.")
            