import sqlite3

# --- DATABASE LOGIC ---

def connect():
    return sqlite3.connect("library.db")

def add_book(title, author_name):
    conn = connect()
    cursor = conn.cursor()
    
    # 1. Check if author exists, if not, add them
    cursor.execute("SELECT id FROM authors WHERE name = ?", (author_name,))
    author = cursor.fetchone()
    
    if not author:
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (author_name,))
        author_id = cursor.lastrowid
    else:
        author_id = author[0]
    
    # 2. Add the book linked to that author ID
    cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", (title, author_id))
    
    conn.commit()
    conn.close()
    print(f"✔️ Added '{title}' by {author_name} to your library!")

def show_books():
    conn = connect()
    cursor = conn.cursor()
    
    # Using a JOIN to get the Author Name instead of just an ID number
    query = """
    SELECT books.id, books.title, authors.name, books.status 
    FROM books 
    JOIN authors ON books.author_id = authors.id
    """
    cursor.execute(query)
    books = cursor.fetchall()
    
    print("\n--- YOUR LIBRARY ---")
    for b in books:
        print(f"ID: {b[0]} | {b[1]} by {b[2]} [{b[3]}]")
    print("--------------------\n")
    conn.close()

def delete_book(book_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print(f"🗑️ Book ID {book_id} deleted.")

# --- USER INTERFACE ---

def main():
    while True:
        print("\n1. Add Book\n2. View Library\n3. Delete Book\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            add_book(title, author)
        elif choice == "2":
            show_books()
        elif choice == "3":
            book_id = input("Enter Book ID to delete: ")
            delete_book(book_id)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
