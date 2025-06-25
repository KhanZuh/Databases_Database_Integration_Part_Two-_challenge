# How to understand this repo
Imagine you have a huge library with thousands of music albums, but instead of walking around looking for albums yourself, you have a helpful librarian (the AlbumRepository) who knows exactly where everything is stored. 

When you want to find albums, you don't talk directly to the library's filing system - instead, you ask the librarian. The librarian then goes to a special computer system (DatabaseConnection) that keeps track of where every single album is located in the library (Database). 

When you ask "show me all the albums," the librarian asks the computer to find every album, and then the computer goes through all the filing cabinets and brings back a big list. The librarian then takes this messy list and organizes it into neat, easy-to-understand album cards (Album objects) before giving them to you. 

If you ask for a specific album by name, the same process happens but the computer only looks for that one album. This way, you get what you need without having to understand how the library's complex filing system works - the librarian handles all the complicated stuff for you!

# Sequence diagram (Mermaid)

![Editor _ Mermaid Chart-2025-06-25-092521](https://github.com/user-attachments/assets/03253d47-937a-45dc-a060-7432585dcef3)



# Overview First
"This diagram shows how a music album database application works, with 6 main components working together to retrieve and display album information."

# Step-by-Step Walkthrough
## Phase 1: Application Startup & Initialization
Step 1-2:

"First, a user types `python app.py` in the Terminal to start the application"
"The `app.py` file begins running and needs to set up a database connection"

### Step 3-5:

"app.py creates a `DatabaseConnection` object and calls `connect()` on it"
"The `DatabaseConnection` reaches out to PostgreSQL and establishes a connection to the 'music_catalog' database"
"The database confirms the connection is successful"

### Step 6-8:

"Next, `app.py` tells the `DatabaseConnection` to seed the database with test data using a SQL file"
"This creates the albums table and fills it with sample album records"
"The database confirms everything is set up properly"

### Step 9-10:

"Finally, `app.py` creates an `AlbumRepository` object, passing in the database connection"
"The repository is now ready to handle album-related operations"

## Phase 2: Getting All Albums
### Step 11-12:

"Now imagine a user wants to see all albums in the database"
"`app.py` calls the `all()` method on the `AlbumRepository`"

### Step 13-15:

"The `AlbumRepository` asks the `DatabaseConnection` to execute a SQL query: `SELECT * from albums`"
"`DatabaseConnection` sends this query to the actual PostgreSQL database"
"The database returns all the album rows as raw data"

### Step 16-19:

The `AlbumRepository` doesn't just return raw database rows"
"Instead, it loops through each row and creates a proper `Album` object for each one"
"Each `Album` object has properties like id, title, release_year, and artist_id"
"Finally, it returns a nice list of `Album` objects back to `app.py`, which displays them to the user"

## Phase 3: Finding a Specific Album
### Step 20-21:

"Now let's say the user wants to find a specific album by its ID"
"`app.py` calls the `find()` method on the `AlbumRepository`, passing in the album ID"

### Step 22-24:

"The `AlbumRepository` creates a more specific SQL query: `SELECT * from albums WHERE id = %s`"
"It safely inserts the album ID into the query (this prevents SQL injection attacks)"
"The database searches for that specific album"

### Step 25-30:

"If the album exists: The database returns the album data, the repository creates an `Album` object, and returns it to be displayed"
"If no album is found: The repository raises an exception saying `'No matches found'`, and the app displays an error message"

## Key Concepts to Emphasize

### Object-Relational Mapping (ORM):
"Notice how we never work with raw database rows directly. The AlbumRepository always converts database data into proper Album objects. This makes the code cleaner and easier to work with."

### Separation of Concerns:
"Each component has a specific job - the Terminal handles user interaction, app.py orchestrates everything, AlbumRepository handles album logic, DatabaseConnection manages database communication, and the Database stores the data."

### Error Handling:
"The system properly handles cases where data might not be found, rather than just crashing."

# Simple Summary
"In essence, this diagram shows how a request flows from the user, through different layers of the application, down to the database, and back up with the results - all while keeping each component focused on its specific responsibility."

