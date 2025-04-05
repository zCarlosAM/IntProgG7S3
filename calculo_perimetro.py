"""
    Cálculo del perímetro y el área de un rectángulo
    Por: Carlos Daniel Aguirre Molina
"""

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area = base * altura

perimetro = (base * 2) + (altura * 2)

print("=" * 50)
print("El área del rectángulo es: ", area)
print("El perímetro del rectángulo es: ", perimetro)
print("=" * 50)