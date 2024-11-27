class albumes:
    def __init__(self, titulo, date, artista):
        self.titulo = titulo #str
        self.date = date #date
        self.artista = artista #str
        #self.albums = []  # Llista d'àlbums
        #artista = artistas 1:1
        #cançons = llista songs 1:N


    def afegir_album(self, album):
        self.albums.append(album)


    def llistar_albums(self):
        for album in self.albums:
            print(f"- {album}")