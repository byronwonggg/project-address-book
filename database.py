import tkinter as tk
from PIL import ImageTk,Image
import sqlite3
from tkinter import ttk 

root = tk.Tk()
root.title('Address Book')
root.geometry("400x600")

# Databases

# create a database or connect to one
conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

# create table
'''
c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer)""")
'''
# Create Function to Edit a record

def update():

    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
        'first': f_name_editor.get(),
        'last': l_name_editor.get(),
        'address': address_editor.get(),
        'city': city_editor.get(),
        'state': state_editor.get(),
        'zipcode': zipcode_editor.get(),
        'oid': record_id
        })

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # close the whole window
    



def edit():
    global editor
    editor = tk.Tk()
    editor.title('editor')
    editor.geometry("400x400")


    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    record_id = delete_box.get()

    # query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # Create Global Varibales for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    #create Text Boxes
    f_name_editor= tk.Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))

    l_name_editor = tk.Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_editor = tk.Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = tk.Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = tk.Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zipcode_editor = tk.Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

  
    #create text box labels
    f_name_label_editor = tk.Label(editor, text="First name")
    f_name_label_editor.grid(row=0, column=0,pady=(10,0))

    l_name_label_editor = tk.Label(editor, text="Last name")
    l_name_label_editor.grid(row=1, column=0)

    address_label_editor = tk.Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)

    city_label_editor = tk.Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)

    state_label_editor = tk.Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)

    zipcode_label_editor = tk.Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)

    # Loop Thru results
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])


    # Create an Save Button
    save_btn = tk.Button(editor, text="Save Records", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)





# Create Function to Delete A record
def delete():
    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    #clear deleteid
    delete_box.delete(0, 'end')



# create submit function for database
def submit():

    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            })

    # commit changes
    conn.commit()

    # close connection
    conn.close()




    # clear the text boxes
    f_name.delete(0,'end')
    l_name.delete(0,'end')
    address.delete(0,'end')
    city.delete(0,'end')
    state.delete(0,'end')
    zipcode.delete(0,'end')

# create query functinon
def query():
    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    # query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)

    # loop thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) +" "+ str(record[1]) +"\t" +str(record[6])+"\n"

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


#create Text Boxes
f_name = tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = tk.Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = tk.Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = tk.Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = tk.Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = tk.Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = tk.Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

#create text box labels
f_name_label = tk.Label(root, text="First name")
f_name_label.grid(row=0, column=0)

l_name_label = tk.Label(root, text="Last name")
l_name_label.grid(row=1, column=0)

address_label = tk.Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = tk.Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = tk.Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = tk.Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = tk.Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = tk.Button(root, text="add record to db", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a query button
query_btn = tk.Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a delete button
delete_btn = tk.Button(root, text="Delete Records", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create an Update Button
edit_btn = tk.Button(root, text="Edit Records", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# commit changes
conn.commit()

# close connection
conn.close()



root.mainloop()