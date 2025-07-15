# main.py
# Entry point for the application. Launches the GUI.

import tkinter as tk
from app import TodoApp

if __name__ == "__main__":
    root = tk.Tk()             # Create window
    app = TodoApp(root)        # Initialize the app with GUI + logic
    root.mainloop()            # Start event loop
