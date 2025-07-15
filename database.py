# database.py
# Handles interaction with the SQLite database for persistent task storage.

import sqlite3
import os

class TaskDatabase:
    def __init__(self, db_file="tasks.db"):
        full_path = os.path.abspath(db_file)
        print(f"[DB Path] Using database at: {full_path}")  # helpful for debugging
        # Connect to the SQLite database file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                name TEXT,
                priority TEXT
            )
        """)
        self.conn.commit()

    def insert_task(self, task_id, name, priority):
        # Insert a task record
        self.cursor.execute(
            "INSERT INTO tasks (id, name, priority) VALUES (?, ?, ?)",
            (task_id, name, priority)
        )
        self.conn.commit()

    def delete_task(self, task_id):
        # Delete a task record
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()

    def get_all_tasks(self):
        # Retrieve all task records
        self.cursor.execute("SELECT id, name, priority FROM tasks")
        return self.cursor.fetchall()
