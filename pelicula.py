"""
    Cálculo del tiempo de la proyección de una película
    Por: Carlos Daniel Aguirre Molina
"""

tiempo_pelicula    = int(input("Ingrese la duración de la película (en minutos): "))
tiempo_comerciales = int(input("Ingrese la duración de los comerciales previos: "))
pausas             = int(input("Ingrese la cantidad de pausas comerciales durante la película: "))
tiempo_pausas      = int(input("Ingrese la duración de cada pausa comercial: "))

total_comerciales  = pausas * tiempo_pausas
tiempo_total       = tiempo_pelicula + tiempo_comerciales + total_comerciales

print("=" * 50)
print(f"Duración original: {tiempo_pelicula}min.")
print(f"Duración de los comerciales en total: {total_comerciales}min.")
print("-" * 50)
print(f"Tiempo total de la proyección: {tiempo_total}min.")
print("=" * 50)