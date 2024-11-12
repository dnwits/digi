# Màxim de tres nombres
# Escriu un programa que trobi el nombre més gran entre tres nombres predefinits i mostri el resultat.
# Dades d'entrada: nombre1 = 15, nombre2 = 9, nombre3 = 12.

nombre1 = 15
nombre2 = 9
nombre3 = 12
if nombre1 > nombre2 and nombre1 > nombre3:
    print("el numero mayor es: ",nombre1)
elif nombre2 > nombre1 and nombre2 > nombre3:
    print("el numero mayor es: ",nombre2)
else: 
    print("el numero mayor es: ",nombre3)
