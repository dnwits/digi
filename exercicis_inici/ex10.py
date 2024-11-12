# Inversor de text
# Escriu un programa que mostri una frase predefinida a l’inrevés.
# Dades d'entrada: frase = "Hola, món!".

frase = "Hola, món!"
frase_inv=""
for x in frase:
    frase_inv= x + frase_inv
print(frase_inv)

for x in range(len(frase)-1,-1,-1):
     print(frase[x])