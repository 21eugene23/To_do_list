To-Do List & Task Tracker
This project is a Python desktop application for managing tasks, built with fundamental data structures and SQLite for data persistence. It offers a CRUD interface for tasks.

🚀 Key Features & Data Structures
The application allows users to:

Add, view, remove tasks.

Undo actions using a Stack.

Prioritize tasks with a Priority Queue.

Perform fast lookups by name using a Hash Table.

Navigate daily tasks with a Linked List.

All task data is saved in an SQLite database for persistence across sessions.

🛠️ Setup & Run
Clone Repository:

git clone https://github.com/ICS-2025-GROUP-F/dsa-sem-project-tottenham.git
cd dsa-sem-project-tottenham

(Replace URL if different)

Virtual Environment (Recommended):

python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # macOS/Linux


Run Application:
GUI Version: python src/GUI.py

Console Version: python src/main.py
(Always run from project root.)

Run Tests:
pytest

(Runs all tests in tests/)

🤝 Git Conventions
Main Branch: main (protected).

Feature Branches: regNo_<YourRegNo>_<ModuleName> (e.g., regNo_P123456_priorityqueue).

Pull Requests (PRs): Merge feature branches to main after teammate review and passing tests.

