import tkinter as tk
from tkinter import messagebox

# ========================
# GLOBAL DATA STRUCTURE
# ========================
tasks = []

# ========================
# FUNCTION
# ========================
def add_task():
    task = entry_task.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "You must enter a task!")
    else:
        tasks.append(task)
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        messagebox.showinfo("Success", f"Task '{task}' added!")

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_index)
        confirm = messagebox.askyesno("Confirm Delete", f"Delete '{task}'?")
        if confirm:
            tasks.remove(task)
            listbox_tasks.delete(selected_index)
            messagebox.showinfo("Deleted", f"Task '{task}' deleted!")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete!")

def view_tasks():
    if not tasks:
        messagebox.showinfo("Tasks", "No tasks found.")
    else:
        all_tasks = "\n".join(tasks)
        messagebox.showinfo("Tasks", f"Your tasks:\n{all_tasks}")

def clear_all_tasks():
    confirm = messagebox.askyesno("Confirm", "Clear all tasks?")
    if confirm:
        tasks.clear()
        listbox_tasks.delete(0, tk.END)
        messagebox.showinfo("Cleared", "All tasks deleted!")

def exit_program():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to quit?")
    if confirm:
        root.destroy()

# ========================
# GUI SETUP
# ========================
root = tk.Tk()
root.title("To-Do App")
root.geometry("400x400")
root.resizable(False, False)

# Title
lbl_title = tk.Label(root, text="📝 TO-DO LIST", font=("Arial", 16, "bold"))
lbl_title.pack(pady=10)

# Entry field
entry_task = tk.Entry(root, width=35, font=("Arial", 12))
entry_task.pack(pady=10)

# Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Add", width=10, command=add_task)
btn_add.grid(row=0, column=0, padx=5)

btn_view = tk.Button(frame_buttons, text="View", width=10, command=view_tasks)
btn_view.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_buttons, text="Delete", width=10, command=delete_task)
btn_delete.grid(row=0, column=2, padx=5)

btn_clear = tk.Button(frame_buttons, text="Clear All", width=10, command=clear_all_tasks)
btn_clear.grid(row=0, column=3, padx=5)

# Task Listbox
listbox_tasks = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
listbox_tasks.pack(pady=10)

# Exit Button
btn_exit = tk.Button(root, text="Exit", width=10, command=exit_program, bg="red", fg="white")
btn_exit.pack(pady=10)

# ========================
# START GUI LOOP
# ========================
root.mainloop()
