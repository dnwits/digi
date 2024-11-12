# Taula de multiplicar
# Escriu un programa que mostri la taula de multiplicar d'un número predefinit fins al 10.
# Dades d'entrada: nombre = 6.
num= input("Indroduzca un número: ")
num=int(num)
for x in range(1,11):
    print(num," x ",x," = ",(num*x))