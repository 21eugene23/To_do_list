# app.py (Member E)
# Combines all data structures and connects them with a graphical user interface (GUI).
# Handles user interactions and updates the backend and database accordingly.

import tkinter as tk
from linked_list import LinkedList          # Task list stored using linked list
from hash_table import HashTable            # Metadata like priority stored in hash table
from undo_stack import Stack                # Stack to support undo/redo actions
from reminder_queue import Queue            # Queue to manage scheduled reminders (not yet shown in UI)
from database import TaskDatabase           # SQLite database interface

class TodoApp:
    def __init__(self, root):
        # Initialize all data structures and database handler
        self.ll = LinkedList()
        self.ht = HashTable()
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.reminder_queue = Queue()
        self.db = TaskDatabase()

        # Set up GUI window
        self.root = root
        self.root.title("To-Do List App - Group F")

        # Input field to type a task
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=5)

        # Button to add a task
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Listbox to show tasks
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=5)

        # Button to delete the selected task
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        # Button to undo the last action (add/delete)
        self.undo_button = tk.Button(root, text="Undo", command=self.undo)
        self.undo_button.pack()

        # Load tasks stored in database into UI on startup
        self.load_from_db()

    def refresh_listbox(self):
        # Clear and repopulate the task list display
        self.task_listbox.delete(0, tk.END)
        for task_id, task_name in self.ll.get_tasks():
            self.task_listbox.insert(tk.END, f"{task_id}: {task_name}")

    def load_from_db(self):
        # Load tasks and their metadata from the SQLite database into the app
        for task_id, name, priority in self.db.get_all_tasks():
            self.ll.add_task(task_id, name)
            self.ht.add_metadata(task_id, {"priority": priority})
        self.refresh_listbox()

    def add_task(self):
        # Add a new task entered by the user
        task_name = self.task_entry.get()
        if task_name:
            task_id = len(self.ll.get_tasks()) + 1  # Auto-generate task ID
            self.ll.add_task(task_id, task_name)    # Add to linked list
            self.ht.add_metadata(task_id, {"priority": "Normal"})  # Add default metadata
            self.db.insert_task(task_id, task_name, "Normal")  # Save to database
            self.undo_stack.push(("add", task_id, task_name))  # Store in undo stack
            self.refresh_listbox()  # Update UI
            self.task_entry.delete(0, tk.END)  # Clear input box

    def delete_task(self):
        # Delete selected task from list and database
        selection = self.task_listbox.curselection()
        if selection:
            selected_text = self.task_listbox.get(selection[0])
            task_id = int(selected_text.split(":")[0])
            task_name = self.ll.get_task_name(task_id)
            if self.ll.delete_task(task_id):  # Remove from linked list
                self.ht.delete_metadata(task_id)  # Remove metadata
                self.db.delete_task(task_id)  # Remove from DB
                self.undo_stack.push(("delete", task_id, task_name))  # Store in undo
                self.refresh_listbox()

    def undo(self):
        # Undo the most recent add/delete action
        if not self.undo_stack.is_empty():
            action, task_id, task_name = self.undo_stack.pop()
            if action == "add":
                # Undo adding: remove task
                self.ll.delete_task(task_id)
                self.ht.delete_metadata(task_id)
                self.db.delete_task(task_id)
                self.redo_stack.push(("add", task_id, task_name))
            elif action == "delete":
                # Undo deletion: re-add task
                self.ll.add_task(task_id, task_name)
                self.ht.add_metadata(task_id, {"priority": "Restored"})
                self.db.insert_task(task_id, task_name, "Restored")
                self.redo_stack.push(("delete", task_id, task_name))
            self.refresh_listbox()
