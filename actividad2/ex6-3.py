# Monitorització intel·ligent d'una granja agrícola
# Descripció: Aquest programa simula el monitoratge d'una granja mitjançant sensors intel·ligents que recullen dades 
# sobre la humitat i la temperatura. Si aquests valors estan fora del rang òptim, el sistema emet una alerta.
#   Input: Valors de temperatura i humitat.
#   Output: Alerta en cas de valors fora del rang òptim.
# Ús pràctic: Millora l'eficiència i la productivitat agrícola al garantir que les condicions de creixement siguin òptimes.


humitatMaxima = 45  
temperaturaMaxima = 50
humitatMin = 30  # Exemple de humitat
temperaturaMin = 35  # Exemple de temperatura
humitat = int(input("Introdueix la humitat: "))
temperatura = float(input("Introdueix la temperatura (°C): "))

if humitat> humitatMaxima or humitat<humitatMin:
    print("¡¡ALERTA!! valors fora del rang òptim...")
elif temperatura>temperaturaMaxima or temperatura<temperaturaMin:
    print("¡¡ALERTA!! valors fora del rang òptim...")
else:
    print("Valor estables i dins dels rangs establerts :3")