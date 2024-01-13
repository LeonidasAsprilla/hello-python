""" Loops
Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages provide loops. Python programming language also provides the following types of two loops:

while loop
for loop """


# Cuenta del 0 hasta el 4
count = 0
while count < 5:
    print(count)
    count = count + 1

# Cuenta del 0 hasta el 5
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# detener el bucle con break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break # detiene el bucle imprimiendo hasta 2


# saltarse la iteración con continue
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1

# ciclo for
# for con listas
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

# for con string
language = 'Python'
for letter in language:
    print(letter)

# for con tuplas
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

# for con diccionarios
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

# for en sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# ejemplo con break
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

# ejemplo con continue
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

""" The Range Function
The range() function is used to loop through a set of code a certain number of times. The range(start,end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range """

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

for number in range(11):
    print(number)   # prints 0 to 10, not including 11

# ciclos embebidos
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# for else - cuando queremos que ejecute algo al finalizar el bucle
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

""" Pass
In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements. """
for number in range(6):
    pass