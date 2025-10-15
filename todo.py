import tkinter as tk
from tkinter import messagebox

tasks =  []
def show_menu():
    print("\n==== TO-DO APP ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            print(f"- {task}")

def add_task():
    
    task= input("enter a new task: ")
    tasks.append(task)
    print(f"Task '{tasks}' added successfully.")
    
def delete_task():
    task = input("enter task to delete: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{tasks}' deleted successfully.")
    else:
        print(f"Task '{tasks}' not found.")

def exit_program():
    print("Goodbye!")
    exit()

def main():
    
    
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    
    
if __name__ == "__main__":
        main()
