"""
    Cálculo del perímetro y el área de un rectángulo
"""

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area = base * altura

base *= 2
altura *= 2
perimetro = base + altura

print("El área del rectángulo es: ", area)
print("El perímetro del rectángulo es: ", perimetro)