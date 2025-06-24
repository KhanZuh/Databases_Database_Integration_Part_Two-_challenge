from lib.album import Album
import pytest

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute ('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"]) # this is called ORM - object relational mapping - converting database rows into objects --> see thinking.txt file for why we create objects
            albums.append(item)
        return albums
    
    def find(self, album_id):
        rows = self._connection.execute('SELECT * from albums WHERE id = %s', [album_id])
        if rows:
            row = rows[0]
            return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
        else:
            raise Exception("No matches found") 
