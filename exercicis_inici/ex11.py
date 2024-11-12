# Conta quantes vegades hi ha una lletra en una cadena.
# Imprimeix la posició quan la trobi.

# Conta quantes A hi ha a la cadena


textdna =  "atggatcattta"
contador=0
vocal="a"
# while p < len(textdna):
#     #print("Posició ",p," ",paraula[p])
#     p+=1
#     if 'a'
# print(textdna," té ",p," lletres")
for x in textdna:
    if x in vocal:
        contador += 1
print("Total de A's: ", contador)