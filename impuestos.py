"""
    Cálculo de precio
    Por: Carlos Daniel Aguirre Molina
"""
precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje del descuento a aplicar: "))
precio_descuento = precio - ((precio * descuento) / 100)

iva = float(input("Ingrese el porcentaje del IVA: "))
iva = (precio_descuento * iva) / 100
precio_final = precio_descuento + iva

print("=" * 50)
print(f"Precio original: {precio} C$")
print(f"Descuento aplicado: {descuento} %")
print(f"Precio con descuento: {precio_descuento} C$")
print(f"IVA calculado: {iva} C$")
print("-" * 50)
print(f"Precio_final: {precio_final} C$")
print("=" * 50)