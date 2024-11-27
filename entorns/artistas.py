class artistas:
    def __init__(self, nom, edad=0):
        self.nom = nom #str
        self.edad = edad 
        self.albums = []  # Llista d'àlbums


    def afegir_album(self, album):
        self.albums.append(album)


    def llistar_albums(self):
        for album in self.albums:
            print(f"- {album}")

a = artistas("Deftones")
a.afegir_album("Koi no Yokai")
print(a.nom)
a.llistar_albums()
# print(a.nom, a.albums)

b = artistas("SZA", 35)
print(b.nom, b.edad)