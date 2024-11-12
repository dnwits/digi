# Gestió de l'eficiència de la cadena de subministrament
# Descripció: El programa calcula el temps total necessari per produir i transportar un producte. 
# Rep com a inputs el temps de producció i el de transport, i retorna el temps total. Això ajuda a mesurar l'eficiència de la cadena de subministrament.
#   Input: Temps de producció i temps de transport.
#   Output: Temps total necessari per a la fabricació i el lliurament del producte.
# Ús pràctic: Permet optimitzar els processos de fabricació i distribució per reduir els retards.

produccio = int(input("Introdueix el temps de producció: "))
t_tra = int(input("Introdueix el temps de transport: "))
t_total= produccio+t_tra
print("El temps total és de ",t_total)