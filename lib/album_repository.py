from lib.album import Album
class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            album = Album(row["id"], row["title"], row['release_year'], row['artist_id'])
            albums.append(album)
        return albums
    
    def find(self, album_id):
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s", [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
    
    def find_album_with_artist(self, album_id):
        rows = self._connection.execute("SELECT albums.id AS albums_id, albums.title, albums.release_year, albums.artist_id, artists.name as artist_name FROM albums JOIN artists ON artists.id = albums.artist_id WHERE albums.id = %s", [album_id])
        row = rows[0]
        return row
    
    def create(self, album):
        self._connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)", [album.title, album.release_year, album.artist_id])