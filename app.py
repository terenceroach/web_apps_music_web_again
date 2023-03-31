import os
from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template, redirect
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection()
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums.html', albums=albums)

@app.route('/albums/<id>')
def get_album(id):
    connection = get_flask_database_connection()
    repository = AlbumRepository(connection)
    album = repository.find_album_with_artist(id)
    return render_template('album.html', album=album)

@app.route('/artists/<id>', methods=['GET'])
def get_artsist(id):
    connection = get_flask_database_connection()
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template('artist.html', artist=artist)

@app.route('/artists', methods=["GET"])
def get_artist_list():
    connection = get_flask_database_connection()
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists.html', artists=artists)

@app.route('/new_album', methods=['GET'])
def get_new_album():
    connection = get_flask_database_connection()
    repository = AlbumRepository(connection)
    return render_template('new_album.html')

@app.route('/albums', methods=['POST'])
def post_new_album():
    connection = get_flask_database_connection()
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    album = Album(None, title, release_year, artist_id)
    repository.create(album)
    return render_template('album.html', album=album)

@app.route('/new_artist', methods=['GET'])
def get_new_artist():
    return render_template("new_artist.html")

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection()
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    repository.create(artist)
    return render_template('artist.html', artist=artist)


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
# from example_routes import apply_example_routes
# apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
