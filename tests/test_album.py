from lib.album import Album
"""
When an album is created
The properties id, title, release_year and artist_id are set
"""
def test_properties():
    album = Album(1, "New album", 2023, 1)
    assert album.id == 1
    assert album.title == 'New album'
    assert album.release_year == 2023
    assert album.artist_id == 1

"""
When 2 albums are creted the same
They are created equal
"""
def test_equality():
    album_1 = Album(1, "New album", 2023, 1)
    album_2 = Album(1, "New album", 2023, 1)
    assert album_1 == album_2

"""
When an album is created
It is nicely formatted
"""
def test_formatting():
    album = Album(1, "New album", 2023, 1)
    assert str(album) == "Album(1, New album, 2023, 1)"