# Retos
""" #1 EL FAMOSO "FIZZ BUZZ"
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """

divisible_por_tres = lambda indice: indice % 3 == 0
divisible_por_cinco = lambda indice: indice % 5 == 0

def fizzbuzz():
    for i in range (1,101):
        if divisible_por_tres(i) and divisible_por_cinco(i):
            print("fizzbuzz")
        elif(divisible_por_tres(i)):
            print("fizz")
        elif(divisible_por_cinco(i)):
            print("buzz")
        else:
            print(i)

# fizzbuzz()
            
""" 
#2
¿ES UN ANAGRAMA?
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 """

def is_anagrama(str1, str2):
    if str1.lower() == str2.lower():
        return False
    return sorted(str1.lower()) == sorted(str2.lower())
    
# print(is_anagrama("Amor", "Roma"))


""" LA SUCESIÓN DE FIBONACCI
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */ """

def fibonacci():
    prev = 0
    next = 1
    for i in range(1,51):
        print(f"{i}: {prev}")   # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
        fib = prev + next       # 1-2-3-5-8-13-21-34-55-89-144-
        prev = next             # 1-1-2-3-5-8-13-21-34-55-89-
        next = fib              # 1-2-3-5-8-13-21-34-55-89-144-

# fibonacci()
        
""" 
#4
¿ES UN NÚMERO PRIMO?
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
 """

# Es un número primo?
def is_primo(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

# print(is_primo(1299709))
# print(is_primo(3951))

# Lista de todos los números primos existentes hasta un número n
def n_primos_hasta(n):
    lista_primos = list()
    for i in range(1,n):
        if is_primo(i):
            lista_primos.append(i)

    print(lista_primos)

# no abusar de n
# n_primos_hasta(4000)

# lista de los primeros n números primos, impresos de 10 en 10
def primeros_n_primos(n):
    lista_primos = list()
    primos = 0
    impresion = 0
    numero = 2
    if n < 1:
        print("Debe pedir al menos un número primo.")
    else:
        while True:                
            if primos == n:
                if impresion > 0:
                    print(lista_primos)
                print(f"Esta fue la lista de los {n} primeros números primos.")
                break
            elif is_primo(numero):
                primos += 1
                impresion += 1
                lista_primos.append(numero)
            if impresion == 10:
                print(lista_primos)
                lista_primos.clear()
                impresion = 0
            numero += 1

# primeros_n_primos(168)

""" 
#7 INVIRTIENDO CADENAS
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
 """

def reverso(texto):
    longitud_texto = len(texto)
    texto_reverso = str()
    for i in range(longitud_texto, 0, -1):
        texto_reverso += texto[i-1]

    return texto_reverso

texto = "Hola Mundo!"
print(len(texto))
print(texto[10])
print(reverso(texto))

# https://retosdeprogramacion.com/