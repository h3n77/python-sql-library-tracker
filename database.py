import sqlite3

def setup_database():
    # This creates the 'library.db' file automatically
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    # Create the Authors table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    """)

    # Create the Books table with a Foreign Key linking to Authors
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER,
        status TEXT DEFAULT 'Unread',
        FOREIGN KEY (author_id) REFERENCES authors (id)
    )
    """)

    connection.commit()
    connection.close()
    print("✨ Database and Tables Created Successfully!")

if __name__ == "__main__":
    setup_database()
