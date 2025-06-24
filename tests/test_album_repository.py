from lib.album_repository import AlbumRepository
from lib.album import Album
import pytest

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    albums = repository.all()
    
    # Assert the length matches expected number of albums
    assert len(albums) == 12
    # Assert the first album has the expected attributes
    expected_album = Album(1, "Doolittle", 1989, 1)
    assert albums[0] == expected_album

# the __eq__ method. in the album class
# The __eq__ method allows us to create an expected album object and compare it directly
# it says  "check if all my attributes match the other album's attributes."
# Instead of writing 4 separate assertions, you can write one clean comparison that checks everything at once!

def test_find_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = repository.find(1)
    expected_album = Album(1, "Doolittle", 1989, 1)
    assert album == expected_album

def test_find_rasies_exception_when_no_match_found(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    with pytest.raises(Exception) as err:
        repository.find(70)
    error_message = str(err.value)
    assert error_message == "No matches found"
