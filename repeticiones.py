import sys
#comprobacion de seguridad, ejecuta si solo se reciben dos argumento reales
if len(sys.argv) == 3:
    cadena = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for repeticiones in range [0,repeticiones]:
        print(cadena)
else:
    print("error - introduce los argumentos correctamente")
    print('por ejemplo: repeticiones.py  "hola" 5')
    