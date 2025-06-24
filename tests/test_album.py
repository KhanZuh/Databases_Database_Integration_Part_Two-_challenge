from lib.album import Album

def test_album_constructs():
    # Test that Album objects are created with the right attributes
    # Check the albums table schema - what columns do you see?
    # Write a test that creates an Album and asserts its attributes match what you expect
    album = Album(1, "Test title", 2020, 5)
    assert album.id == 1
    assert album.title == "Test title"
    assert album.release_year == 2020
    assert album.artist_id == 5

def test_album_equality():
    album1 = Album(1, "Doolittle", 1989, 1)
    album2 = Album(1, "Doolittle", 1989, 1)
    assert album1 == album2
    
    album3 = Album(2, "Different Album", 2020, 2)
    assert album1 != album3

def test_album_repr():
    album = Album(1, "Doolittle", 1989, 1)
    assert str(album) == "Album(1, Doolittle, 1989, 1)"

