from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_text = task_entry.get()
    if len(task_text) == 0:
        messagebox.showinfo('Error', 'Task field is empty')
    else:
        tasks.append(task_text)
        the_cursor.execute('INSERT INTO Tasks VALUES (?)', (task_text,))
        update_tasks()
        task_entry.delete(0, 'end')

def update_tasks():
    clear_tasks()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        if selected_task in tasks:
            tasks.remove(selected_task)
            update_tasks()
            the_cursor.execute('DELETE FROM tasks WHERE title = ?', (selected_task,))
    except TclError:
        messagebox.showinfo('Error', 'No task selected.')

def delete_all_tasks():
    confirm_delete = messagebox.askyesno('Delete All', 'Are you sure you want to delete all tasks?')
    if confirm_delete:
        tasks.clear()
        the_cursor.execute('DELETE FROM tasks')
        update_tasks()
        messagebox.showinfo('Delete All', 'All tasks deleted')

def clear_tasks():
    task_listbox.delete(0, 'end')

def close_app():
    print(tasks)
    window.destroy()

def retrieve_tasks():
    tasks.clear()
    for row in the_cursor.execute('SELECT Title FROM Tasks'):
        tasks.append(row[0])

# Main

if __name__ == "__main__":
    window = Tk()
    window.title("Task Manager")
    window.geometry("750x400")
    window.resizable(0, 0)
    window.configure(bg="#E0E0E0")

    connection = sql.connect('ListOfTasks.db')
    the_cursor = connection.cursor()
    the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks(title TEXT)')

    tasks = []

    function_frame = Frame(window, bg="#E0E0E0")
    function_frame.pack(side="top", expand=True, fill="both")

    task_label = Label(function_frame, text="Enter Task:", font=("Arial", 14, "bold"), bg="#E0E0E0", fg="#004080")
    task_label.grid(row=0, column=0, padx=10, pady=10)

    task_entry = Entry(function_frame, font=("Arial", 14), width=42, fg="#004080", bg="white")
    task_entry.grid(row=0, column=1, padx=10, pady=10)

    add_button = Button(function_frame, text="Add Task", width=11, height=2, bg="#FFD699", font=("Arial", 14, "bold"), command=add_task)
    delete_button = Button(function_frame, text="Delete Task", width=11, height=2, bg="#FFD699", font=("Arial", 14, "bold"), command=delete_task)
    delete_all_button = Button(function_frame, text="DelAllTasks", width=11, height=2, bg="#FFD699", font=("Arial", 14, "bold"), command=delete_all_tasks)
    exit_button = Button(function_frame, text="Exit", width=52, height=2, bg="#FFD699", font=("Arial", 14, "bold"), command=close_app)

    add_button.grid(row=1, column=0, pady=10)
    delete_button.grid(row=1, column=1, pady=10)
    delete_all_button.grid(row=1, column=2, pady=10)
    
    task_listbox = Listbox(function_frame, width=57, height=7, font=("Arial", 12), selectmode='SINGLE', bg='white', fg='#004080', selectbackground="#FFD699", selectforeground="#004080")
    task_listbox.grid(row=2, column=0, columnspan=3, pady=10)

    retrieve_tasks()
    update_tasks()
    window.mainloop()
    connection.commit()
    the_cursor.close()
