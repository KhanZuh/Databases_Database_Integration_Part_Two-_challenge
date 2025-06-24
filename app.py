from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

try:
    # Setup
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/music_library.sql")
    

    # Get all albums using the AlbumRepository
    album_repository = AlbumRepository(connection)
    for album in album_repository.all():
        print(album)

    # Find and print album
    album_repository = AlbumRepository(connection)
    album = album_repository.find(1)
    print(f"✓ Found album: {album}")
    
except Exception as e:
    print(f"✗ {e}")