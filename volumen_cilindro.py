"""
    Cálculo del volumen de un cilindro
    Por: Carlos Daniel Aguirre Molina
"""

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area_base = 3.14 * (radio * radio)
volumen = area_base * altura
area_lateral = 2 * 3.14 * radio * altura
area_superficial = area_lateral + (area_base * 2)

print("=" * 50)
print(f"Radio: {radio}")
print(f"Altura: {altura}")
print("-" * 50)
print(f"Volumen: {volumen}")
print(f"Área superficial: {area_superficial}")
print("=" * 50)