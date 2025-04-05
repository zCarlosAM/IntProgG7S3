"""
    Cálculo del salario neto de un empleado
    Por: Carlos Daniel Aguirre Molina
"""

sal_bruto = float(input("Ingrese el salario en bruto del empleado: "))

renta = sal_bruto * 0.1 
seguro = sal_bruto * 0.05
pensiones = sal_bruto * 0.03

descuento = renta + seguro + pensiones
sal_neto = sal_bruto - descuento

print()
print("------------------------------------")
print("INFORMACIÓN DEL EMPLEADO")
print("------------------------------------")
print("Salario neto:", sal_neto)
print("------------------------------------")
print("Descuentos")
print("------------------------------------")
print("Impuesto sobre la renta:", renta)
print("Seguro social:", seguro)
print("Fondo de pensiones:", pensiones)
print("Total:", descuento)
print("------------------------------------")
print("Salario neto:", sal_neto)
print("------------------------------------")