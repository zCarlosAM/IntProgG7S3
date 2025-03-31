"""
    Calculate the note of a student based on three systematic evaluations.
    The note is the sum of the three evaluations.
"""

sistematico1 = int(input("Ingrese la nota del primer sistemático (Máximo 30):"))
sistematico2 = int(input("Ingrese la nota del segundo sistemático (Máximo 30):"))
sistematico3 = int(input("Ingrese la nota del tercer sistemático (Máximo 40):"))

nota = (sistematico1 + sistematico2 + sistematico3)
print("La nota del estudiante es:", nota)