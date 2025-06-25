# How to understand this repo
Imagine you have a huge library with thousands of music albums, but instead of walking around looking for albums yourself, you have a helpful librarian (the AlbumRepository) who knows exactly where everything is stored. 

When you want to find albums, you don't talk directly to the library's filing system - instead, you ask the librarian. The librarian then goes to a special computer system (DatabaseConnection) that keeps track of where every single album is located in the library (Database). 

When you ask "show me all the albums," the librarian asks the computer to find every album, and then the computer goes through all the filing cabinets and brings back a big list. The librarian then takes this messy list and organizes it into neat, easy-to-understand album cards (Album objects) before giving them to you. 

If you ask for a specific album by name, the same process happens but the computer only looks for that one album. This way, you get what you need without having to understand how the library's complex filing system works - the librarian handles all the complicated stuff for you!

# Sequence diagram (Mermaid)

![Editor _ Mermaid Chart-2025-06-25-092521](https://github.com/user-attachments/assets/03253d47-937a-45dc-a060-7432585dcef3)


This sequence diagram illustrates how a music library application retrieves album data from a PostgreSQL database using a layered architecture pattern. 

The flow begins when a user runs the application from the terminal, which triggers the main `app.py` program to initialize a database connection and seed it with test data from a SQL file. The application then creates an `AlbumRepository` instance that acts as an intermediary between the application logic and the database. 

When users request album information, there are two main operations: retrieving all albums using the `all()` method, which executes a SELECT query and converts each database row into an `Album` object before returning a list to the user; and finding a specific album using the `find()` method, which uses a parameterized query to search by ID and either returns a single `Album` object or raises an exception if no match is found. 

Throughout this process, the `DatabaseConnection` class handles all direct database interactions, while the `AlbumRepository` implements the Object-Relational Mapping (ORM) pattern by transforming raw database rows into meaningful Python objects, creating a clean separation between the database layer and the application logic.
