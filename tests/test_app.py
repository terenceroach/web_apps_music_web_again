from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection
# Tests for your routes go here

"""
GET /albums
Returns albums
"""
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    p_tags = page.locator("p")
    
    expect(h2_tags).to_have_text([
        "Title: Doolittle",
        "Title: Surfer Rosa",
        "Title: Waterloo",
        "Title: Super Trouper",
        "Title: Bossanova",
        "Title: Lover",
        "Title: Folklore",
        "Title: I Put a Spell on You",
        "Title: Baltimore",
        "Title: Here Comes the Sun",
        "Title: Fodder on My Wings",
        "Title: Ring Ring"
        ])
    
    expect(p_tags).to_contain_text([
        "Released: 1989",
        "Released: 1988",
        "Released: 1974",
        "Released: 1980",
        "Released: 1990",
        "Released: 2019",
        "Released: 2020",
        "Released: 1965",
        "Released: 1978",
        "Released: 1971",
        "Released: 1982",
        "Released: 1973"]
        )
    
"""
GET /album
Return 1 album with a given id
"""
def test_get_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    p_tag = page.locator("p")

    expect(p_tag).to_have_text(["Release year: 1989\nArtist: Pixies"])

"""
GET albums/<id>
Return the information about the album corresponding to id
"""
def test_visit_album_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Waterloo'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Waterloo")

"""
GET artists/<id>
Return details for a single artist
"""
def test_get_single_artist_details(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text(["Name: Pixies\nGenre: Rock"])

"""
GET /artists
Returns artists
"""
def test_get_artists_list(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/artists")
    h2_tags = page.locator("h2")
    p_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        "Name: Pixies",
        "Name: ABBA",
        "Name: Taylor Swift",
        "Name: Nina Simone"
        ])
    expect(p_tags).to_have_text([
        "Genre: Rock",
        "Genre: Pop",
        "Genre: Pop",
        "Genre: Jazz"
        ])
    
"""
GET artists/<id>
Return the information about the artist corresponding to id
"""
def test_visit_artist_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Taylor Swift'")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text(["Name: Taylor Swift\nGenre: Pop"])

"""
GET /albums_new
Return a form to add new album
"""
def test_new_album_form(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/new_album")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("New Album")

"""
POST /albums
Adds a valid album
"""
def test_post_new_album_created(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/new_album")
    page.fill('#title', 'My New Album')
    page.fill('#release_year', '2023')
    page.fill('#artist_id', '2')
    page.click('input[type="submit"]')
    page.goto(f"http://{test_web_address}/albums")
    p_tag = page.locator("p")
    expect(p_tag).to_contain_text(["2023"])

"""
create a new artist
"""
def test_create_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click('text="Add artist"')
    page.fill('input[name=name]', "Test Artist")
    page.fill('input[name=genre]', "Dance")
    page.click('text="Add artist"')
    p_tag = page.locator("p")
    expect(p_tag).to_have_text(["Name: Test Artist\nGenre: Dance"])

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
