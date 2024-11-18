# array: 
# llista=[1,5,7,9]
# print(llista[2])
# printa el elemento en la posición 2 (0,1,2)

# Aquest programa simula un sistema de ciberseguretat en una planta industrial digitalitzada. 
# Monitoritza intents d'accés als sistemes, diferenciant entre usuaris autoritzats i no autoritzats. 
# Si es detecta un accés no autoritzat, emet un avís d'alerta.

accessos = {'usuari1': 'autoritzat', 'usuari2': 'no autoritzat'}
#print(accessos['usuari1'])
usuari = str(input("Introdueix l'usuari: "))
print(accessos[usuari])