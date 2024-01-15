# Condicionales
# if
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
    
# if else
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# If Elif Else

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# en una linea
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

# si anidado
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# condicional si con operadores logicos
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')