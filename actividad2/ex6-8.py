#Explicació pas a pas:
# 1- Menú: El programa mostra un menú d'opcions perquè l'usuari pugui triar què vol fer.
# 2- Afegir producte: Afegeix un nou producte a la llista inventari amb la quantitat introduïda per l'usuari.
# 3- Eliminar producte: L'usuari pot introduir el nom del producte que vol eliminar, i si es troba, s'elimina de la llista.
# 4- Actualitzar quantitat: Permet canviar la quantitat d'un producte existent. Si el producte no existeix, 
# mostra un missatge d'error.
# 5- Consultar inventari: Mostra tots els productes amb la seva quantitat actual.
# 6- Sortir: Finalitza el programa quan l'usuari selecciona l'opció 5.

# Llista inicial d'inventari amb alguns productes (nom, quantitat)
inventari = [["Poma", 50], ["Plàtan", 30], ["Taronja", 20]]


while True:
    print("\n--- Menú d'Inventari ---")
    print("1. Afegir producte")
    print("2. Eliminar producte")
    print("3. Actualitzar quantitat")
    print("4. Consultar inventari")
    print("5. Sortir")

    opcio=input("Escull l'opció: ")
    if opcio == '1':
        print("Afegir producte")
        p=input("Introdueixi producte: ")
        q=int(input("Introdueixi quantitat: "))
        inventari.append([p,q])
    elif opcio == '2' :
        print("Eliminar producte")
        nom=input("Introdueixi el producte a eliminar: ")
        for producte in inventari:
            if producte[0]==nom:
                inventari.remove(producte)
                print("Producte eliminat :3c")
                break
    elif opcio == '3' :
        print("Actualitzar quantitat")
    elif opcio == '4' :
        print("Consultar inventari")
        for x in range(0, len(inventari)):
            print(inventari[x][0],"amb quantitat: ",inventari[x][1])
        #FORMA CORERCTA EN PYTHON:
        # for producte in inventari:
        #     print(producte[0], "quantitat: ",producte[1])
    elif opcio == '5' :
        print("dew :3")
        break
    
