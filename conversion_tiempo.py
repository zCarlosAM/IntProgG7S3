"""
    Conversión de tiempo
    Por: Carlos Daniel Aguirre Molina
"""

segundos = int(input("Ingrese la cantidad total de segundos: "))

horas = segundos // 3600
segundos -= (horas * 3600)
minutos = segundos // 60
segundos -= (minutos * 60)

print("El tiempo total son:", horas, "horas, ", minutos, "minutos y", segundos, "segundos.")