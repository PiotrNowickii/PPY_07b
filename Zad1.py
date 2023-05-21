import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk


def load_data():
    try:
        conn = sqlite3.connect('studenci.db')
        cursor = conn.cursor()
        data = cursor.execute("SELECT * FROM studenci")
        for item in my_tree.get_children():
            my_tree.delete(item)
        for row in data:
            my_tree.insert("", "end", values=(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
            row[13], row[14], row[15], row[16], row[17], row[18], row[19]))
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def open_details_window(event):
    selected_item = my_tree.focus()

    if selected_item:
        item_data = my_tree.item(selected_item)
        item_values = item_data["values"]

        details_window = tkinter.Toplevel(root)
        details_window.title("Szczegóły")

        id_label = ttk.Label(details_window, text="ID:")
        id_label.pack()
        id_entry = ttk.Entry(details_window)
        id_entry.insert(0,item_values[0])
        id_entry.config(state="disabled")
        id_entry.pack()

        email_label = ttk.Label(details_window, text="Email:")
        email_label.pack()
        email_entry = ttk.Entry(details_window)
        email_entry.insert(0, item_values[1])
        email_entry.pack()

        name_label = ttk.Label(details_window, text="Name:")
        name_label.pack()
        name_entry = ttk.Entry(details_window)
        name_entry.insert(0, item_values[2])
        name_entry.pack()

        surname_label = ttk.Label(details_window, text="Surname:")
        surname_label.pack()
        surname_entry = ttk.Entry(details_window)
        surname_entry.insert(0, item_values[3])
        surname_entry.pack()

        project_label = ttk.Label(details_window, text="Project:")
        project_label.pack()
        project_entry = ttk.Entry(details_window)
        project_entry.insert(0, item_values[4])
        project_entry.pack()

        l_1_label = ttk.Label(details_window, text="l_1")
        l_1_label.pack()
        l_1_entry = ttk.Entry(details_window)
        l_1_entry.insert(0, item_values[5])
        l_1_entry.pack()

        l_2_label = ttk.Label(details_window, text="l_2")
        l_2_label.pack()
        l_2_entry = ttk.Entry(details_window)
        l_2_entry.insert(0, item_values[6])
        l_2_entry.pack()

        l_3_label = ttk.Label(details_window, text="l_3")
        l_3_label.pack()
        l_3_entry = ttk.Entry(details_window)
        l_3_entry.insert(0, item_values[7])
        l_3_entry.pack()

        h_1_label = ttk.Label(details_window, text="h_1")
        h_1_label.pack()
        h_1_entry = ttk.Entry(details_window)
        h_1_entry.insert(0, item_values[8])
        h_1_entry.pack()

        h_2_label = ttk.Label(details_window, text="h_2")
        h_2_label.pack()
        h_2_entry = ttk.Entry(details_window)
        h_2_entry.insert(0, item_values[9])
        h_2_entry.pack()

        h_3_label = ttk.Label(details_window, text="h_3")
        h_3_label.pack()
        h_3_entry = ttk.Entry(details_window)
        h_3_entry.insert(0, item_values[10])
        h_3_entry.pack()

        h_4_label = ttk.Label(details_window, text="h_4")
        h_4_label.pack()
        h_4_entry = ttk.Entry(details_window)
        h_4_entry.insert(0, item_values[11])
        h_4_entry.pack()

        h_5_label = ttk.Label(details_window, text="h_5")
        h_5_label.pack()
        h_5_entry = ttk.Entry(details_window)
        h_5_entry.insert(0, item_values[12])
        h_5_entry.pack()

        h_6_label = ttk.Label(details_window, text="h_6")
        h_6_label.pack()
        h_6_entry = ttk.Entry(details_window)
        h_6_entry.insert(0, item_values[13])
        h_6_entry.pack()

        h_7_label = ttk.Label(details_window, text="h_7")
        h_7_label.pack()
        h_7_entry = ttk.Entry(details_window)
        h_7_entry.insert(0, item_values[14])
        h_7_entry.pack()

        h_8_label = ttk.Label(details_window, text="h_8")
        h_8_label.pack()
        h_8_entry = ttk.Entry(details_window)
        h_8_entry.insert(0, item_values[15])
        h_8_entry.pack()

        h_9_label = ttk.Label(details_window, text="h_9")
        h_9_label.pack()
        h_9_entry = ttk.Entry(details_window)
        h_9_entry.insert(0, item_values[16])
        h_9_entry.pack()

        h_10_label = ttk.Label(details_window, text="h_10")
        h_10_label.pack()
        h_10_entry = ttk.Entry(details_window)
        h_10_entry.insert(0, item_values[17])
        h_10_entry.pack()

        grade_label = ttk.Label(details_window, text="grade")
        grade_label.pack()
        grade_entry = ttk.Entry(details_window)
        grade_entry.insert(0, item_values[18])
        grade_entry.pack()

        status_label = ttk.Label(details_window, text="Status:")
        status_label.pack()
        status_entry = ttk.Entry(details_window)
        status_entry.insert(0, item_values[19])
        status_entry.pack()
        def update():
            try:
                conn = sqlite3.connect('studenci.db')
                cursor = conn.cursor()
                id = id_entry.get()
                email = email_entry.get()
                namee = name_entry.get()
                surname = surname_entry.get()
                project = project_entry.get()
                l_1 = l_1_entry.get()
                l_2 = l_2_entry.get()
                l_3 = l_3_entry.get()
                h_1 = h_1_entry.get()
                h_2 = h_2_entry.get()
                h_3 = h_3_entry.get()
                h_4 = h_4_entry.get()
                h_5 = h_5_entry.get()
                h_6 = h_6_entry.get()
                h_7 = h_7_entry.get()
                h_8 = h_8_entry.get()
                h_9 = h_9_entry.get()
                h_10 = h_10_entry.get()
                grade = grade_entry.get()
                status = status_entry.get()
                query = "UPDATE studenci SET email = ?, namee = ?, surname = ?, project = ?, l_1 = ?, l_2 = ?, l_3 = ?, h_1 = ?, h_2 = ?, h_3 = ?, h_4 = ?, h_5 = ?, h_6 = ?, h_7 = ?, h_8 = ?, h_9 = ?, h_10 = ?, grade = ?, status = ? WHERE id = ?"
                p = (
                    email, namee, surname, project, l_1, l_2, l_3, h_1, h_2, h_3, h_4, h_5, h_6, h_7, h_8, h_9, h_10, grade,
                    status, id)
                cursor.execute(query, p)
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            load_data()
            details_window.destroy()
        update = ttk.Button(details_window, text="Edytuj", command=update)
        update.pack()
        def delete():
            try:
                id = id_entry.get()
                conn = sqlite3.connect('studenci.db')
                cursor = conn.cursor()

                query = 'DELETE FROM  studenci WHERE id = ?'
                p = (id)
                cursor.execute(query, p)
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            load_data()
            details_window.destroy()
        delete = ttk.Button(details_window, text="Usuń", command=delete)
        delete.pack()


def new_student_window():
    new_window = tkinter.Toplevel(root)
    new_window.title("Dodaj nowego studenta")

    email_label = ttk.Label(new_window, text="email")
    email_label.pack()
    email_entry = ttk.Entry(new_window)
    email_entry.pack()

    name_label = ttk.Label(new_window, text="name")
    name_label.pack()
    name_entry = ttk.Entry(new_window)
    name_entry.pack()

    surname_label = ttk.Label(new_window, text="surname")
    surname_label.pack()
    surname_entry = ttk.Entry(new_window)
    surname_entry.pack()

    project_label = ttk.Label(new_window, text="project")
    project_label.pack()
    project_entry = ttk.Entry(new_window)
    project_entry.pack()

    l_1_label = ttk.Label(new_window, text="l_1")
    l_1_label.pack()
    l_1_entry = ttk.Entry(new_window)
    l_1_entry.pack()

    l_2_label = ttk.Label(new_window, text="l_2")
    l_2_label.pack()
    l_2_entry = ttk.Entry(new_window)
    l_2_entry.pack()

    l_3_label = ttk.Label(new_window, text="l_3")
    l_3_label.pack()
    l_3_entry = ttk.Entry(new_window)
    l_3_entry.pack()

    h_1_label = ttk.Label(new_window, text="h_1")
    h_1_label.pack()
    h_1_entry = ttk.Entry(new_window)
    h_1_entry.pack()

    h_2_label = ttk.Label(new_window, text="h_2")
    h_2_label.pack()
    h_2_entry = ttk.Entry(new_window)
    h_2_entry.pack()

    h_3_label = ttk.Label(new_window, text="h_3")
    h_3_label.pack()
    h_3_entry = ttk.Entry(new_window)
    h_3_entry.pack()

    h_4_label = ttk.Label(new_window, text="h_4")
    h_4_label.pack()
    h_4_entry = ttk.Entry(new_window)
    h_4_entry.pack()

    h_5_label = ttk.Label(new_window, text="h_5")
    h_5_label.pack()
    h_5_entry = ttk.Entry(new_window)
    h_5_entry.pack()

    h_6_label = ttk.Label(new_window, text="h_6")
    h_6_label.pack()
    h_6_entry = ttk.Entry(new_window)
    h_6_entry.pack()

    h_7_label = ttk.Label(new_window, text="h_7")
    h_7_label.pack()
    h_7_entry = ttk.Entry(new_window)
    h_7_entry.pack()

    h_8_label = ttk.Label(new_window, text="h_8")
    h_8_label.pack()
    h_8_entry = ttk.Entry(new_window)
    h_8_entry.pack()

    h_9_label = ttk.Label(new_window, text="h_9")
    h_9_label.pack()
    h_9_entry = ttk.Entry(new_window)
    h_9_entry.pack()

    h_10_label = ttk.Label(new_window, text="h_10")
    h_10_label.pack()
    h_10_entry = ttk.Entry(new_window)
    h_10_entry.pack()

    grade_label = ttk.Label(new_window, text="grade")
    grade_label.pack()
    grade_entry = ttk.Entry(new_window)
    grade_entry.pack()

    status_label = ttk.Label(new_window, text="status")
    status_label.pack()
    status_entry = ttk.Entry(new_window)
    status_entry.pack()

    def insert():
        email = email_entry.get()
        namee = name_entry.get()
        surname = surname_entry.get()
        project = project_entry.get()
        l_1 = l_1_entry.get()
        l_2 = l_2_entry.get()
        l_3 = l_3_entry.get()
        h_1 = h_1_entry.get()
        h_2 = h_2_entry.get()
        h_3 = h_3_entry.get()
        h_4 = h_4_entry.get()
        h_5 = h_5_entry.get()
        h_6 = h_6_entry.get()
        h_7 = h_7_entry.get()
        h_8 = h_8_entry.get()
        h_9 = h_9_entry.get()
        h_10 = h_10_entry.get()
        grade = grade_entry.get()
        status = status_entry.get()

        try:
            conn = sqlite3.connect('studenci.db')
            cursor = conn.cursor()

            query = 'INSERT INTO studenci (email, namee, surname, project, l_1, l_2, l_3, h_1, h_2, h_3, h_4, h_5, h_6, h_7, h_8, h_9, h_10, grade, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            p = (email, namee, surname, project, l_1, l_2, l_3, h_1, h_2, h_3, h_4, h_5, h_6, h_7, h_8, h_9, h_10, grade, status)
            cursor.execute(query, p)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        load_data()
        new_window.destroy()
        return

    insert_button = ttk.Button(new_window, text="Dodaj", command=insert)
    insert_button.pack()


root = Tk()
root.title('Baza studentów')
root.geometry("1500x500")

tree_frame = Frame(root)
tree_frame.pack(pady=10)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")

tree_scroll.config(command=my_tree.yview)

my_tree["columns"] = ("ID", "email", "namee", "surname","project", "l_1", "l_2", "l_3", "h_1", "h_2", "h_3", "h_4", "h_5", "h_6", "h_7", "h_8", "h_9", "h_10", "grade", "status")
my_tree.column("#0", width=0)
my_tree.column("ID", width=20)
my_tree.column("namee", width=60)
my_tree.column("surname", width=60)
my_tree.column("project", width=40)
my_tree.column("l_1", width=40)
my_tree.column("l_2", width=40)
my_tree.column("l_3", width=40)
my_tree.column("h_1", width=40)
my_tree.column("h_2", width=40)
my_tree.column("h_3", width=40)
my_tree.column("h_4", width=40)
my_tree.column("h_5", width=40)
my_tree.column("h_6", width=40)
my_tree.column("h_7", width=40)
my_tree.column("h_8", width=40)
my_tree.column("h_9", width=40)
my_tree.column("h_10", width=40)
my_tree.column("grade", width=40)



my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("email", text="email", anchor=CENTER)
my_tree.heading("namee", text="name", anchor=CENTER)
my_tree.heading("surname", text="surname", anchor=CENTER)
my_tree.heading("project", text="project", anchor=CENTER)
my_tree.heading("l_1", text="l_1", anchor=CENTER)
my_tree.heading("l_2", text="l_2", anchor=CENTER)
my_tree.heading("l_3", text="l_3", anchor=CENTER)
my_tree.heading("h_1", text="h_1", anchor=CENTER)
my_tree.heading("h_2", text="h_2", anchor=CENTER)
my_tree.heading("h_3", text="h_3", anchor=CENTER)
my_tree.heading("h_4", text="h_4", anchor=CENTER)
my_tree.heading("h_5", text="h_5", anchor=CENTER)
my_tree.heading("h_6", text="h_6", anchor=CENTER)
my_tree.heading("h_7", text="h_7", anchor=CENTER)
my_tree.heading("h_8", text="h_8", anchor=CENTER)
my_tree.heading("h_9", text="h_9", anchor=CENTER)
my_tree.heading("h_10", text="h_10", anchor=CENTER)
my_tree.heading("grade", text="grade", anchor=CENTER)
my_tree.heading("status", text="status", anchor=CENTER)
my_tree.pack()

add_new_student_button = tkinter.Button(root, text="Dodaj nowego studenta", command=new_student_window)
add_new_student_button.pack()

my_tree.bind("<Double-1>",open_details_window)
try:
    conn = sqlite3.connect('studenci.db')
    create_table_query = "CREATE TABLE IF NOT EXISTS studenci(" \
                         "id INTEGER PRIMARY KEY AUTOINCREMENT," \
                         "email TEXT," \
                         "namee TEXT," \
                         "surname TEXT," \
                         "project INTEGER," \
                         "l_1 INTEGER," \
                         "l_2 INTEGER," \
                         "l_3 INTEGER," \
                         "h_1 INTEGER," \
                         "h_2 INTEGER," \
                         "h_3 INTEGER," \
                         "h_4 INTEGER," \
                         "h_5 INTEGER," \
                         "h_6 INTEGER," \
                         "h_7 INTEGER," \
                         "h_8 INTEGER," \
                         "h_9 INTEGER," \
                         "h_10 INTEGER," \
                         "grade INTEGER," \
                         "status TEXT)"

    cursor = conn.cursor()
    cursor.execute(create_table_query)
    conn.commit()
    data = cursor.execute("SELECT * FROM studenci")
except sqlite3.Error as e:
    print(f"Error: {e}")
for row in data:
    my_tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19]))
root.mainloop()
