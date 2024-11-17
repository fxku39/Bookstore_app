# Bookstore_app
Python project to create a Bookstore database with a GUI so the user can add, delete, update and search entries in the database. 

### Background for Project
We wanted to create a program in a .exe file for a Bookstore where they can add, delete, update and search for books and also the program itself creates and manages the database. 

### Methodology
We used the tkinter library to create the GUI and defined every element first so we can have our blueprint already formatted. Then we created the Backend section utilizing sqlite3 for the creation of the Database (db) and doing the respective queries for each button in the GUI.
1. First we started with the "Connection function" which is in charge of creating the db and see if the Table for our db is already created. 
2. Then the "Insert function" to add new entries to our table.
3. Next we created a "View function" so we can inspect in the app what elements exists in the our db.
4. We added the next functions: "Search, Delete and Update" so the user can search entries in our db.
5. Finally we connected the backend with the frontend and now the program it's functional.

![GUI](https://github.com/user-attachments/assets/79983a4d-abfb-4e47-aa71-60d17751ca0b)

### Conclusions
The app already works and each function do what is intended at first sight, we can add entries, delete them, search for entries in our db and change/update this elements but there's a lot of room for improvement.

### Updates and next Features
At this stage that we call v1.0 the app works but it needs more refining in the frontend and the backend.
First in the backend we need better control of what the user is capable of doing and not, here are some examples:
* If the user try to add a new book or entry, the program needs to ask for all the entry labels and if one or more are missing give an alert with this information and not add the element, this ensures the db won't have any empty elements.
* When the user try to delete something from the db the program need to ask him if he accepts or not to commit these changes.
* When the user search for an element in our db he need to know the exact data (title, author, year, isbn). If he has a typo error the program is not going to retrieve that information, this is caused by our sql query combined with sintaxis format in python + sqlite3. A proposal to fix this is using if statement + sql command LIKE with markdowns in our search function.

Then the frontend need a better style and some fixes in the sizes and positioning of each element, like entry spaces with the labels and the listbox. Another thing is that we want to present the information in the listbox as a table with the name of each columns and not as rows with each element concatenated. Finally we want to add a function so our program do a copy of the db in another folder for backups, it can be daily backups at the same time and save each one as a different archive in case of unexpected errors don't lose all the information.
