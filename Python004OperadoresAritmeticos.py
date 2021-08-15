"""
Comentario multilinea

Operacion           Symbol
---------------     ------
Suma                  +
Resta                 -
Multiplicacion        *
Division              /
Division entera       //
Exponente             **
Modulo                 %

"""
operandoA = int(input('Ingrese un numero: '))
operandoB = int(input('Ingresa un numero: '))
suma = operandoA + operandoB
print('La suma es:', suma)

# imprimiendo con format
print(f'La suma es: {suma}')

resta = operandoA - operandoB
print(f'La resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'La resta es: {multiplicacion}')

division_flotante = operandoA / operandoB
print(f'La resta es: {division_flotante}')

division_entera = operandoA // operandoB
print(f'La resta es: {division_entera}')

exponente = int(input('Ingrese el numero de potencia: '))
print(f'La potencia de {operandoA} es {operandoA**exponente}')
print(f'La potencia de {operandoB} es {operandoB**exponente}')

modulo = int(input('Ingrese el modulo: '))
print(f'El modulo de {operandoA} es {operandoA%modulo}')
print(f'El modulo de {operandoB} es {operandoB%modulo}')

# calcular el area y perimetro de un rectangulo (alto, ancho)
alto = int(input('Proporciona el alto: '))
ancho = int(input('Proporciona el ancho: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'Area: {area}\nPerimetro: {perimetro}')

# Operadores de asignacion
miVariable = 10
print(miVariable)
miVariable = miVariable + 1
print(miVariable)
# incremento con reasignacion
miVariable += 1
print(miVariable)
miVariable -= 2
print(miVariable)
miVariable *= 3
print(miVariable)
miVariable /= 2
print(miVariable)

# Operadores de comparacion
a = int(input('Ingrese un numero: '))
b = int(input('Ingrese un numero: '))
resultado = a == b
print(f'Resultado == : {resultado}')
resultado = a != b
print(f'Resultado != : {resultado}')
resultado = a > b
print(f'Resultado > : {resultado}')
resultado = a >= b
print(f'Resultado >= : {resultado}')
resultado = a < b
print(f'Resultado > : {resultado}')
resultado = a <= b
print(f'Resultado >= : {resultado}')

# Ejercicio numero par o impar
a = int(input('Por favor ingrese un numero: '))
if a % 2 == 0:
    print(f'{a} es un número par')
else:
    print(f'{a} no es un número par')

# Ejercicio mayor de edad
edad = int(input('Escribe tu edad: '))
if edad >= 18:
    print(f'Eres mayor de edad {edad}')
else:
    print(f'Eres menor de edad {edad}')

# Operadores lógicos
"""
Operador    Descripcion                             Uso
--------    -------------------------------------   ---------
and         Devuelve True si ambos son True         a and b
or          Devuelve True si alguno es True         a or b
not         Devuelve True si alguno es False        not a
--------    -------------------------------------   ---------
"""
a = True
b = True
resultado = a and b
print(f'a and b = {resultado}')
resultado = a or b
print(f'a or b = {resultado}')
resultado = not a
print(f'not a = {resultado}')

# Ejercicio valor dentro de rango(0-5)
numero = int(input('Ingrese un numero: '))
if numero >= 0 and numero <= 5:
    print(f'{numero} se encuentra en el rango (0 - 5)')
else:
    print(f'{numero} no se encuentra en el rango (0 - 5)')

# Ejercicio asistencia de padre a hijo
vacaciones = False
diaDescanso = False
if vacaciones or diaDescanso:
    print('El padre puede asistir al juego del hijo')
else:
    print('El padre no puede asistir al juego del hijo')

vacaciones = False
diaDescanso = False
if not (vacaciones or diaDescanso):
    print('El padre puede asistir al juego del hijo')
else:
    print('El padre no puede asistir al juego del hijo')

# Ejercicio rango de edad entre 20's o 30's usando condicional if anidada
edad = int(input('Proporciona tu edad: '))
if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print(f'Tu edad de {edad} años ,se encuentra dentro del rango de 20\'s o 30\'s')
    if edad >= 20 and edad < 30:
        print('Se encuentra dentro de los 20\'s')
    elif edad >= 30 and edad < 40:
        print('Se encuentra dentro de los 30\'s')
else:
    print(f'Tu edad de {edad} años ,no se encuentra dentro del rango de 20\'s o 30\'s')

#Ejercicio el mayor de dos numeros(numero1, numero2)
numero1 = int(input('Proporcioma el numero1: '))
numero2 = int(input('Proporciona el numero2: '))
if numero1 == numero2:
    print('Ambos numeros son iguales')
elif numero1 > numero2:
    print(f'El numero mayor es: {numero1}')
else:
    print(f'El numero mayor es: {numero2}')

# Ejercicio de Tienda de libros
nombreLibro = input('Proporcione los siguientes datos del libro:\nProporcione el nombre del libro: ')
idLibro = int(input('Proporcione el ID: '))
precioLibro = round(float(input('Proporcione el precio: ')), 2)
envioLibro = bool(input('Indique si el envio es gratuito (True / False): '))
print(f'Nombre: {nombreLibro}\nId: {idLibro}\nPrecio: {precioLibro}\nEnvio gratuito: {envioLibro}')

