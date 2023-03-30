import os
from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository

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
