#tipo: int
x = 10
print(x)
print(type(x))

#tipo: float
x = 15.62
print(x)
print(type(x))

#tipo: String
x = 'Esta es una cadena'
print(x)
print(type(x))

#tipo: boolean
x = True
print(x)
print(type(x))

miGrupoFavorito = 'Aerosmith'
print('Mi grupo favorito es: ' + miGrupoFavorito)

miGrupoFavorito = 'Metallica'
comentario = 'The best Rock Band'
print('Mi grupo favorito es: ' + miGrupoFavorito + ' ' + comentario)

miGrupoFavorito = 'Morat'
comentario = 'La mejor banda psicologica'
# la coma automaticamente le pone un espacio a la impresion en consola
print('Mi grupo favorito es:', miGrupoFavorito, comentario)

numero1 = '1'
numero2 = '2'
print('concatenacion', numero1 + numero2)

# convertir valores
print('Suma:', int(numero1) + int(numero2))

numero1 = 1
numero2 = 2
print(numero1 + numero2)

# tipos boolean (bool)
miVariable = True
print(miVariable)

miVariable = False
print(miVariable)

# expresiones bool
miVariable = 1 > 2
print(miVariable)

miVariable = 2 > 1
print(miVariable)

# introduccion a condicional if
if miVariable:
    print('El resultado fue verdadero')
else:
    print('El resultado fue falso')

# procesar entrada de datos por consola (input)
# Funcion input para procesar la entrada de usuario
resultado = input('Escribe un mensaje: ')
print('Valor proporcionado:', resultado)
print('Fin del programa')

numero1 = input('Escribe un numero: ')
numero2 = input('Escribe un numero: ')
resultado = numero1 + numero2
print('El resultado es:', resultado)

numero1 = int(input('Escribe un numero: '))
numero2 = int(input('Escribe un numero: '))
resultado = numero1 + numero2
print('La suma es:', resultado)

# Ejercicio de como estuvo tu dia (1 - 10)
dia = int(input('¿Como estuvo tu día? (0 - 10): '))
print('Mi dia estuvo de:', dia)

# Ejercicio - se solicita la siguiente informacion acerca de un libro(titulo,autor)
titulo = input('Proporciona el título: ')
autor = input('Proporciona el autor: ')
print(titulo, 'fue escrito por', autor)
