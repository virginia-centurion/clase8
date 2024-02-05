# Agenda de contactos
# Crear un menu con las opciones de agendar contacto y ver informacion de contacto.
# Para agendar se solicitara al usuario un: nombre, apellido, telefono, direccion.
# Para ver informacion se pedira el nombre y apellido.
# La informacion sera un listado de diccionarios, donde cada diccionario tendra como 
# claves lo solicitado al usuario y como valor lo que ingrese el usuario. A su vez, 
# este listado debe estar guardado en un archivo json.




import json

def obtener_agenda():
    try:
        with open(f'agenda.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError as e:
        return []

def agendar():
    agenda = obtener_agenda()
    contacto = {
        'nombre': input('Ingrese su nombre: '),
        'apellido': input('Ingrese su apellido: '),
        'telefono': input('Ingrese su telefono: '),
        'direccion': input('Ingrese su direccion: '),
    }
    agenda.append(contacto)
    with open(f'agenda.json', 'w') as archivo:
        json.dump(agenda, archivo, indent=4)
        
def ver_contacto():
    nombre_a_buscar = input('Ingrese nombre: ')
    apellido_a_buscar = input('Ingrese apellido: ')
    agenda = obtener_agenda()
    for contacto in agenda:
        if contacto['nombre'] != nombre_a_buscar or contacto['apellido'] != apellido_a_buscar:
            continue
        print(f"""
    Nombre: {contacto['nombre']}
    Apeliido: {contacto['apellido']}
    Telefono: {contacto['telefono']}
    Direccion: {contacto['direccion']}
    """)
        break
    else:
        print(f'No se encontro el contacto {nombre_a_buscar} {apellido_a_buscar}.')

def menu():
  print('''Menu
  1. Agendar contacto.
  2. Ver contacto.
  ''')
  opcion = input('Ingrese opcion: ')
  if opcion not in ['1','2']:
    print('No ingreso ninguna opcion valida.')
    return
  if opcion == '1':
    agendar()
  elif opcion == '2':
    ver_contacto()

menu()
