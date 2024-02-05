from clases import Alumno

# Primer módulo
# Hacer una clase fácil, como Alumno, con nombre y nota, con un método imprimir().
# Crear una instancia de Alumno, mostrando sus datos y llamando al método desde otro módulo.

alumno = Alumno('Ricardo', '7')
print(alumno.nombre)
print(alumno.nota)
print(alumno.imprimir())