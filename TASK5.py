import re
from functools import partial
from tkinter import *
from tkinter import ttk, messagebox
import pymysql

# User Credentials
db_host = "localhost"
db_user = "root"
db_password = "siddhant"
db_name = "contact_book"

color_primary = "deep sky blue"
color_secondary = "gray95"
color_text = "black"
color_background = "white"
color_warning = "red"
color_success = "green3"
font_primary = "times new roman"
font_secondary = "helvetica"

columns = ("first_name", "last_name", "address", "contact", "email")

def is_valid_email(email):
    email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # Username
    @                       # @Symbol
    [a-zA-Z0-9.-]+          # Domain Name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)
    
    email_address = email_regex.findall(email)
    return bool(email_address)

class ContactManagementApp:
    def __init__(self, root):
        self.window = root
        self.window.title("Contact Book")
        self.window.geometry("940x480")
        self.window.config(bg=color_background)
        
        # Customization
        self.color_primary = color_primary
        self.color_secondary = color_secondary
        self.color_text = color_text
        self.color_background = color_background
        self.color_warning = color_warning
        self.color_success = color_success
        self.font_primary = font_primary
        self.font_secondary = font_secondary
        self.columns = columns

        # User Credentials
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name

        # Left Frame
        self.frame_left = Frame(self.window, bg=color_primary)
        self.frame_left.place(x=0, y=0, width=740, relheight=1)

        # Right Frame
        self.frame_right = Frame(self.window, bg=color_secondary)
        self.frame_right.place(x=740, y=0, relwidth=1, relheight=1)

        # Buttons
        self.add_new_btn = Button(self.frame_right, text='Add New', font=(font_primary, 12), bd=2, command=self.add_contact, cursor="hand2", bg=color_secondary, fg=color_text)
        self.add_new_btn.place(x=50, y=40, width=100)

        self.display_btn = Button(self.frame_right, text='Display', font=(font_primary, 12), bd=2, command=self.display_contacts, cursor="hand2", bg=color_secondary, fg=color_text)
        self.display_btn.place(x=50, y=100, width=100)

        self.search_btn = Button(self.frame_right, text='Search', font=(font_primary, 12), bd=2, command=self.search_contact, cursor="hand2", bg=color_secondary, fg=color_text)
        self.search_btn.place(x=50, y=160, width=100)

        self.clear_btn = Button(self.frame_right, text='Clear', font=(font_primary, 12), bd=2, command=self.clear_screen, cursor="hand2", bg=color_secondary, fg=color_text)
        self.clear_btn.place(x=50, y=340, width=100)

        self.exit_btn = Button(self.frame_right, text='Exit', font=(font_primary, 12), bd=2, command=self.exit_app, cursor="hand2", bg=color_secondary, fg=color_text)
        self.exit_btn.place(x=50, y=400, width=100)

    def selected_contact(self, event):
        self.update_btn = Button(self.frame_right, text='Update', font=(font_primary, 12), bd=2, command=self.update_contact, cursor="hand2", bg=color_success, fg=color_text)
        self.update_btn.place(x=50, y=220, width=100)

        self.delete_btn = Button(self.frame_right, text='Delete', font=(font_primary, 12), bd=2, command=self.delete_contact, cursor="hand2", bg=color_warning, fg=color_text)
        self.delete_btn.place(x=50, y=280, width=100)

    def display_contacts(self):
        self.clear_screen()

        scroll_x = ttk.Scrollbar(self.frame_left, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_left, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_left, columns=self.columns, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        scroll_x.pack(side=BOTTOM, fill=X)

        for column in self.columns:
            self.tree.heading(column, text=column.capitalize(), anchor=W)

        self.tree.pack()
        self.tree.bind('<Double-Button-1>', self.selected_contact)

        try:
            connection = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)
            curs = connection.cursor()
            curs.execute("select * from contact_register")
            rows = curs.fetchall()

            if rows:
                for index, row in enumerate(rows):
                    self.tree.insert("", 'end', text=(index + 1), values=row)
            else:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)

            connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def show_contacts(self, rows):
        self.clear_screen()

        scroll_x = ttk.Scrollbar(self.frame_left, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_left, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_left, columns=self.columns, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        scroll_x.pack(side=BOTTOM, fill=X)

        for column in self.columns:
            self.tree.heading(column, text=column.capitalize(), anchor=W)

        self.tree.pack()
        self.tree.bind('<Double-Button-1>', self.selected_contact)

        for index, row in enumerate(rows):
            self.tree.insert("", 'end', text=(index + 1), values=row)

    def add_contact(self):
        pass  # Add your implementation here

    def update_contact(self):
        pass  # Add your implementation here

    def delete_contact(self):
        pass  # Add your implementation here

    def search_contact(self):
        pass  # Add your implementation here

    def clear_screen(self):
        pass  # Add your implementation here

    def exit_app(self):
        pass  # Add your implementation here

if __name__ == "__main__":
    root = Tk()
    app = ContactManagementApp(root)
    root.mainloop()
