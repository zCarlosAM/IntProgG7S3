"""
    Conversión de temperatura
    Por: Carlos Daniel Aguirre Molina
"""

grado_f = float(input("Ingrese una temperatura en grados Fahrenheit: "))

grado_c = (grado_f - 32) * 5 / 9
grado_k = grado_c + 273.15

print("=" * 50)
print("En grados celcius: ", grado_c)
print("En grados Kelvin: ", grado_k)