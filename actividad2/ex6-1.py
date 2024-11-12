# Calculadora d'estalvi en la digitalització d'una empresa
# Descripció: Aquest programa simula la implementació d'un projecte de digitalització en una empresa i calcula l'estalvi potencial obtingut. 
# L'objectiu és rebre com a input els costos abans i després de la digitalització i retornar l'estalvi total en euros i el percentatge de reducció de costos.
#   Input: Cost abans i després de la digitalització.
#   Output: Estalvi total i percentatge d'estalvi.
# Ús pràctic: Aquest tipus de càlcul és útil per avaluar l'eficiència de la transformació digital en termes de reducció de costos.

cost_abans = float(input("Entra el cost abans de la digitalització (€): "))

cost_despres = float(input("Entra el cost després de la digitalització (€): "))


estalvi= cost_abans - cost_despres
percentatge = (estalvi*100/cost_abans)
print("L'estalvi total es de ",estalvi," €")
print("El percentatge d'estalvi es del ",percentatge," %")