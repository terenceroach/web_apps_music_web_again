from lib.album_repository import AlbumRepository
from lib.album import Album
"""
When I call #all on AlbumRepository
A list of all the albums is returned
"""
def test_all(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result == [
        Album(1, 'Invisible Cities', 1990, 1),
        Album(2, 'The Man Who Was Thursday', 2004, 2),
        Album(3, 'Bluets', 1999, 3),
        Album(4, 'No Place on Earth', 2016, 4)
    ]

"""
When I call #find on AlbumRepository with an id
I get the Album corresponding to that id back
"""
def test_find(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    result = repository.find(2)
    assert result == Album(2, 'The Man Who Was Thursday', 2004, 2)

"""
When I call #create on the AlbumRepository with some fields
And then I list out all the albums
The new album is in the list
"""
def test_create(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'New album', 2023, 5)
    repository.create(album)
    result = repository.all()
    assert result == [
        Album(1, 'Invisible Cities', 1990, 1),
        Album(2, 'The Man Who Was Thursday', 2004, 2),
        Album(3, 'Bluets', 1999, 3),
        Album(4, 'No Place on Earth', 2016, 4),
        Album(5, 'New album', 2023, 5)
    ]