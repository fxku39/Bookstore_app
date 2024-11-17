from tkinter import *
import bookstoreback

# We define a function to select rows so we can delete that row from our db or update and fill the labels with that information

def get_selected_row(event):
    try:
        global selected_tuple # Declaration of global variable so we can use it in the function delete
        index=list1.curselection()[0] # This line of code retrieves the number of the index of the element we click on our listbox
        selected_tuple = list1.get(index) # This line of code retrieves the entire elements as a tuple based of the index number of each row
        # Then we delete and insert the information of the row we clicked on each label space
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


## We create a function to link our view button with our view function in the backend and
## ensure when we click it, it displays the entire database and doesn't repeat itself for each click
def view_command():
    list1.delete(0,END)
    for row in bookstoreback.view():
        list1.insert(END, row)

## 
def search_command():
    list1.delete(0,END)
    for row in bookstoreback.search(title_ent.get(), author_ent.get(), year_ent.get(), isbn_ent.get()):
        list1.insert(END, row)

## We create a function to link our add entry button with out insert function in the backend
## 
def add_command():
    bookstoreback.insert(title_ent.get(), author_ent.get(), year_ent.get(), isbn_ent.get())
    list1.delete(0,END)
    list1.insert(END, (title_ent.get(), author_ent.get(), year_ent.get(), isbn_ent.get()))


def delete_command():
    bookstoreback.delete(selected_tuple[0])


def update_command():
    bookstoreback.update(selected_tuple[0], title_ent.get(), author_ent.get(), year_ent.get(), isbn_ent.get())    
    print(selected_tuple[0])

## We create our Tkinter object
window = Tk()
window.wm_title('Bookstore')

## Labels for each text entry window with their positioning

l1= Label(window, text= "Title")
l1.grid(row=0, column=0)

l2= Label(window, text= "Author")
l2.grid(row=0, column=2)

l3= Label(window, text= "Year")
l3.grid(row=1, column=0)

l4= Label(window, text= "ISBN")
l4.grid(row=1, column=2)

## Entry

title_ent=StringVar()
e1= Entry(window, textvariable=title_ent)
e1.grid(row=0, column=1)

author_ent=StringVar()
e2= Entry(window, textvariable=author_ent)
e2.grid(row=0, column=3)

year_ent=StringVar()
e3= Entry(window, textvariable=year_ent)
e3.grid(row=1, column=1)

isbn_ent=StringVar()
e4= Entry(window, textvariable=isbn_ent)
e4.grid(row=1, column=3)

## Creation of the listbox

list1=Listbox(window, height=15, width=30)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

## Creation of a scrollbar to view all the elements in listbox
sb1= Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

## Link between the scrollbar and the list
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

## Creation of each button

b1=Button(window, text='View all', width=14, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text='Search entry', width=14, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text='Add entry', width=14, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text='Update', width=14, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text='Delete', width=14, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text='Close', width=14, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()