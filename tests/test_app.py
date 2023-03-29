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
    div_tags = page.locator("div")
    # p_tag = page.locator("p")
    
    expect(div_tags).to_have_text([
        "Title: Invisible Cities\nReleased: 1990",
        "Title: The Man Who Was Thursday\nReleased: 2004",
        "Title: Bluets\nReleased: 1999",
        "Title: No Place on Earth\nReleased: 2016"])

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
