"""
    Cálculo de masa corporal
    Por: Carlos Daniel Aguirre Molina
"""

peso = float(input("Ingresa el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))

altura = altura
imc = peso / (altura * altura)
imc = round(imc, 2)

if imc < 18.5:
    clasif = "Bajo peso"
elif imc >= 18.5 and imc <= 24.9:
    clasif = "Peso normal"
elif imc >= 25 and imc <= 29.9:
    clasif = "Sobrepeso"
elif imc >= 30 and imc <= 34.9:
    clasif = "Obesidad Grado I"
elif imc >= 35 and imc <= 39.9:
    clasif = "Obesidad Grado II"
elif imc >= 40 and imc <= 49.9:
    clasif = "Obesidad Grado III"
elif imc >= 50:
    clasif = "Obesidad Grado IV"

print("=" * 50)
print(f"Peso ingresado: {peso}kg")
print(f"Altura ingresada: {altura}m")
print(f"IMC calculado: {imc}")
print("-" * 50)
print(f"La clasificación de su IMC es: {clasif}")
print("=" * 50)