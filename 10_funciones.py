# Funciones

# Funciones sin parametros
def generate_full_name ():
    first_name = 'Leonidas'
    last_name = 'Asprilla'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 5
    num_two = 8
    total = num_one + num_two
    print(total)
add_two_numbers()

# Funciones que retornan un valor
def generate_full_name ():
    first_name = 'Leonidas'
    last_name = 'Asprilla'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

# Funciones con parametros
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Leonidas'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return(total)

print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Funciones con dos parametros
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Leonidas','Asprilla'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Este año cumpliras: ', calculate_age(2024, 1981))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

# paso de argumentos llave:valor
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return(full_name)
print(print_fullname(firstname = 'Leonidas', lastname = 'Asprilla'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    return(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter

# ejemplo retornando boolean
def es_par (n):
    if n % 2 == 0:
        print('par')
        return True    # return stops further execution of the function, similar to break 
    return False
print(es_par(10)) # True
print(es_par(7)) # False

# Returning a list:
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

# Funciones con parametros por defecto
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Leonidas'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('Leonidas','Asprilla'))

def calculate_age (birth_year,current_year = 2024):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1981))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object on the surface of the moon in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon

# Número arbitrario de argumentos
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

# Default and Arbitrary Number of Parameters in Functions
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

# Función como parametro de otra función
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27

""" Moure continua con clases. Quedan pendiente las dias 12-20 de Asabeneh en 30 Days of Python """