# Compara els caràcters d’una cadena amb una altra
# Guarda el número de caràcters que són iguals en la mateixa posició.

# Coincideixen H i l el resultat és 2
text =  "Hello World"
text2 = "Hola mon!!!"  
coincide = 0

# Recorremos ambas cadenas al mismo tiempo
for i in range(min(len(text), len(text2))):
    if text[i] == text2[i]:
        coincide += 1

print("El número de caracteres iguales en la misma posición es:", coincide)