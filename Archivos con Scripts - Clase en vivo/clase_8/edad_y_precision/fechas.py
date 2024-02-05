from datetime import datetime

# Edad y precision
# Calcular tu edad con la mayor precisión posible y cuantos
# segundos faltan para tu cumpleaños. Utilizando un módulo llamado fechas.py.

dia = int(input('Ingrese dia (numero) de nacimiento: '))
mes = int(input('Ingrese mes (numero) de nacimiento: '))
anio = int(input('Ingrese año de nacimiento: '))

hoy = datetime.now()
nacimiento = datetime(anio, mes, dia)

tiempo = hoy - nacimiento
print(tiempo)
anios = tiempo.days // 365
meses = (tiempo.days % 365) // 30 # aproximado
dias = (tiempo.days % 365) % 30
horas = tiempo.seconds // 3600
min = (tiempo.seconds % 3600) // 60
seg = (tiempo.seconds % 360) % 60

print(f'Tenes Años: {anios}, meses: {meses}, dias: {dias}, horas: {horas}, minutos: {min}, segundos: {seg}.')

proximo = datetime(hoy.year + 1, mes, dia)
(proximo - hoy).total_seconds

print(f'Faltan {(proximo - hoy).total_seconds()} seg para tu cumpleaños.')

