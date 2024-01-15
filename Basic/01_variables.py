# Variables
my_string_variable = "My String variable"
print(my_string_variable)

# Variables in Python
first_name = 'Leonidas'
last_name = 'Asprilla'
country = 'Colombia'
city = 'Ciénaga'
age = 42
is_married = False
skills = ['HTML', 'CSS', 'JS', 'Laravel', 'Python']
person_info = {
   'firstname':'Leonidas',
   'lastname':'Asprilla',
   'country':'Colombia',
   'city':'Ciénaga'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Variables en una sola linea
nombre, apellido, alias, edad = "Leonidas", "Asprilla", "Omicron", 42
print(f"Me llamo: {nombre} {apellido}, tengo {edad} años y me dicen {alias}.")

# Obteniendo datos de entrada de texto

""" first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age) """

# Conversión de tipos de datos
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_float', float(num_str))  # 10.6
# print('num_int', int(num_str))      # 10 # ValueError: invalid literal for int() with base 10: '10.6'

# str to list
first_name = 'Leonidas'
print(first_name)               # 'Leonidas'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['L', 'e', 'o', 'n', 'i', 'd', 'a', 's']