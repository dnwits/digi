# Simulador de manteniment predictiu
# Descripció: El manteniment predictiu és una pràctica important a la indústria digitalitzada. 
# Aquest programa rep dades sobre l'ús d'una màquina com les hores treballades, la temperatura i les vibracions, 
# i decideix si cal o no manteniment segons uns llindars establerts. Si alguna de les variables supera els límits, el sistema alerta que es necessita manteniment.
#   Input: Hores d'ús, temperatura i vibracions.
#   Output: Missatge indicant si cal manteniment o no.
# Ús pràctic: Això ajuda a preveure fallades de màquines abans que passin, reduint el temps d'inactivitat i els costos de reparació inesperats.

hores = int(input("Introdueix les hores treballades: "))
temperatura = float(input("Introdueix la temperatura (°C): "))
vibracions = float(input("Introdueix les vibracions (unitats): "))

horesMaximes = 14
temperaturaMaxima = 80
vibracionMaxima = 25
if temperatura > temperaturaMaxima:
    print("Cal manteniment")
elif hores > horesMaximes:
    print("Cal manteniment")
elif vibracions > vibracionMaxima:
    print("Cal manteniment")
else:
    print("No cal manteniment")