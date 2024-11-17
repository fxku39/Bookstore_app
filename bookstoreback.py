import sqlite3
## We define each function to create and use the database so it can connect later with the gui (frontend) and do those queries
## things to improve: Create the database and also make a copy everyday at the same time so we can have a backup database in case of any error.

# First we create the database if not exists already
def connect():
    conn=sqlite3.connect("Bookstore\Bookstore.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER) ")
    conn.commit()
    conn.close()


# We create a function to insert new values in the database
def insert(title, author, year, isbn):
    conn=sqlite3.connect("Bookstore\Bookstore.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES(NULL, ?,?,?,?)", (title, author, year,isbn))
    conn.commit()
    conn.close()


# We create a function so wee can see in the gui the actual database
def view():
    conn=sqlite3.connect("Bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    output_all = cur.fetchall()
    conn.close()
    return output_all

# We create a search function so the user can search a book by his different attributes
def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("Bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year=? OR isbn=?",(title, author,year,isbn))
    output_all=cur.fetchall()   
    conn.close()
    return output_all


# We create a function so the user can delete entrys in the database
# Things to improve: Launch a warning window asking if the user is sure to realize this changes in this database
def delete(id):
    conn=sqlite3.connect("Bookstore.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()


# We create a function to update
def update(id, title, author, year, isbn):
    conn=sqlite3.connect("Bookstore.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn, id))
    conn.commit()
    conn.close() 

