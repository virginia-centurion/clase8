# Tablas
# Desarrollar:
# * Una función que pida un número entero y guarde en un fichero con el nombre 
#   tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.
# * Una funcion que pida un número entero, lea el fichero tabla-n.txt 
#   con la tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

# Estas 2 funciones deben ser seleccionadas por el usuario dentro de un menu.

# En este caso hice todo con funciones para dar otro ejemplo
# de como poder resolver los problemas
def generar(numero):
  datos = open(f'tabla-{numero}.txt', 'w')
  for i in range(1,11):
    datos.write(f'{numero} x {i} = {numero*i}\n')
  datos.close()
  
def mostrar(numero):
  try:
    datos = open(f'tabla-{numero}.txt', 'r')
    print(datos.read())
    datos.close()
  except FileNotFoundError as e:
    print('No se encontro el archivo correspondiente.')

def menu():
  print('''Menu
  1. Generar tabla de multiplicar.
  2. Mostrar tabla de multiplicar.
  ''')
  opcion = input('Ingrese opcion: ')
  if opcion not in ['1','2']:
    print('No ingreso ninguna opcion valida.')
    return
  num = int(input('Ingrese numero a operar:'))
  if opcion == '1':
    generar(num)
  elif opcion == '2':
    mostrar(num)

menu()



# Otra opcion
# Agregar al ejemplo anterior una opcion que pida dos números n y m, lea 
# el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por
# pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por 
# pantalla informando de ello y consultando si se desea generar.

# En este caso hice todo con funciones para dar otro ejemplo
# de como poder resolver los problemas
def generar(numero):
  datos = open(f'tabla-{numero}.txt', 'w')
  for i in range(1,11):
    datos.write(f'{numero} x {i} = {numero*i}\n')
  datos.close()

def mostrar(numero):
  try:
    datos = open(f'tabla-{numero}.txt', 'r')
  except FileNotFoundError as e:
    print('No se encontro el archivo correspondiente.')
  print(datos.read())
  datos.close()
  
def buscar_linea(numero):
  linea = int(input('Ingrese linea (1 a 10):'))
  try:
    datos = open(f'tabla-{numero}.txt', 'r')
    lineas = datos.readlines()
    print(lineas[linea-1])
    datos.close()
  except FileNotFoundError as e:
    print('No se encontro el archivo correspondiente.')
    confirmacion = input('Desea generar la tabla? ("si" para confirmar)').lower()
    if confirmacion == 'si': 
        generar(numero)
        buscar_linea(numero)

def menu():
  print('''Menu
  1. Generar tabla de multiplicar.
  2. Mostrar tabla de multiplicar.
  3. Mostrar linea de la tabla de multiplicar.
  ''')
  opcion = input('Ingrese opcion: ')
  if opcion not in ['1','2','3']:
    print('No ingreso ninguna opcion valida.')
    return
  num = int(input('Ingrese numero a operar:'))
  if opcion == '1':
    generar(num)
  elif opcion == '2':
    mostrar(num)
  elif opcion == '3':
    buscar_linea(num)

menu()