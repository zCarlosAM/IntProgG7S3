"""
    Cambio de monedas
    Por: Carlos Daniel Aguirre Molina
"""
dinero = float(input("Ingrese una cantidad en dólares: "))

dolares_euros = 0.91
dolares_libras = 0.78
dolares_yenes = 145.53 

dinero_euros = dinero * dolares_euros
dinero_libras = dinero * dolares_libras
dinero_yenes = dinero * dolares_yenes

print("=" * 50)
print(f"Cantidad original en dólares: {dinero}")
print("-" * 50)
print(f"Cantidad en euros: {dinero_euros}")
print(f"Cantidad en libras: {dinero_libras}")
print(f"Cantidad en yenes: {dinero_yenes}")
print("=" * 50)