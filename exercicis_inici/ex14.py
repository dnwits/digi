# Inverteix una paraula iterant la cadena

text =  "hola"
frase_inv=""
for x in text:
    frase_inv= x + frase_inv
print(frase_inv)

for x in range(len(text)-1,-1,-1):
     print(text[x])