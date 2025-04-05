"""
    Cálculo de la duración de un viaje
    Por: Carlos Daniel Aguirre Molina
"""

tramo1 = int(input("Ingrese la duración del primer tramo del vuelo (minutos): "))
escala1 = int(input("Ingrese la duración de la primera escala: "))

tramo2 = int(input("Ingrese la duración del segundo tramo del vuelo: "))
escala2 = int(input("Ingrese la duración de la segunda escala: "))

tramo3 = int(input("Ingrese la duración del tercer tramo del vuelo: "))
tiempo_total = tramo1 + escala1 + tramo2 + escala2 + tramo3

print("-" * 50)
print(f"Tiempo total del viaje: {tiempo_total} minutos")
print("-" * 50)