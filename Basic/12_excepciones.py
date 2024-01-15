# Manejo de excepciones
""" try:
    print(10 + '5')
except:
    print('Something went wrong')

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2024 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured') 

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2024 - int(year_born)
    print('You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.') 


try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
"""

# captura de la información de la excepción

try:
    print(1 + "2")
    print("No se ha producido un error")
except ValueError as error:
    print(f"Se ha producido un error de tipo ValueError: {error}") # solo si es un ValueError
except TypeError as error:
    print(f"Se ha producido un error de tipo TypeError: {error}") # solo si es un TypeError
except Exception as error:
    print(f"Se ha producido un error no manejado: {error}") # Todos los demas errores
