# LibreTrack: Python & SQL Library Manager

A robust command-line application designed to bridge the gap between **relational databases** and **Python logic**. This project demonstrates how to architect a database schema, manage data integrity, and perform complex queries using SQL.

---

##  Key Features
* **Relational Data Mapping:** Uses Foreign Keys to link Authors to their specific Books.
* **Full CRUD Operations:** Create, Read, Update, and Delete records in real-time.
* **Persistent Storage:** Data is saved in a local `.db` file, so your library is never lost.
* **Status Tracking:** Mark books as "Reading," "Completed," or "Wishlist."

---

## Tech Stack
* **Language:** Python 3.x
* **Database:** SQLite3 (Relational Database Management System)
* **Architecture:** Modular design with separate database and logic layers.

---

##  Database Schema
The project utilizes two tables with a One to Many relationship:

1.  **Authors Table:** `id` (PK), `name`
2.  **Books Table:** `id` (PK), `title`, `author_id` (FK), `status`

---

## Sample SQL Query
One of the core logic challenges was joining tables to display human-readable data. Here is the query used to fetch books along with their respective authors:

```sql

initial REAME setup
SELECT books.title, authors.name, books.status 
FROM books 
JOIN authors ON books.author_id = authors.id;
