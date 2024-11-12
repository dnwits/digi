# Comptador de lletres
# Escriu un programa que compti el nombre de lletres en una paraula predefinida i mostri el resultat.
# Dades d'entrada: paraula = "programació".

paraula = "programació"
p=0
while p < len(paraula):
    #print("Posició ",p," ",paraula[p])
    p+=1
print(paraula," té ",p," lletres")