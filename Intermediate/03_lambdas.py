# Lambdas - Funciones anónimas
# Función Lambda para calcular el cuadrado de un número
square = lambda x: x ** 2
print(square(3)) # Resultado: 9

# Funcion tradicional para calcular el cuadrado de un numero
def square1(num):
  return num ** 2
print(square(5)) # Resultado: 25

lambda_func = lambda x: x**2 # Funcion que recoge un número entero y devuelve su cuadrado
print(lambda_func(3)) # Retorna 9

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtrado = filter(lambda x: x % 2 != 0, mi_lista)

print(list(filtrado))
# [1, 3, 5, 7, 9]

""" 
Ejemplo 1
Por ejemplo, puedes escribir una función lambda que duplique sus argumentos lambda x: x * 2 y usarla con la función map para duplicar todos los elementos de una lista:
 """
mi_lista = [1, 2, 3, 4, 5, 6]
lista_nueva = list(map(lambda x: x * 2, mi_lista))
print(lista_nueva)  # [2, 4, 6, 8, 10, 12]

""" 
Ejemplo 2
También puedes escribir una función lambda que revise si un número es positivo, lambda x: x > 0, y usarla con la función filter para crear una lista de números positivos.
 """
mi_lista = [18, -3, 5, 0, -1, 12]
lista_nueva = list(filter(lambda x: x > 0, mi_lista))
print(lista_nueva) # [18, 5, 12]

""" 
Ejemplo 3
También es posible que una función devuelva una función lambda.

Si necesitas funciones que multipliquen diferentes números, por ejemplo, duplicar, triplicar, etc... una función lambda puede ser útil

En lugar de crear múltiples funciones, puedes crear una sola función multiplicar_por() y llamarla con diferentes argumentos para crear una función que duplique o triplique.
 """
def multiplicar_por (n):
  return lambda x: x * n
  
duplicar = multiplicar_por(2)
triplicar = multiplicar_por(3)
diez_veces = multiplicar_por(10)

print(duplicar(6)) # 12
print(triplicar(5)) # 15
print(diez_veces(12)) # 120

