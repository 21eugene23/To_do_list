# hash_table.py
# Stores task metadata such as priority using a Python dictionary.

class HashTable:
    def __init__(self):
        self.table = {}

    def add_metadata(self, task_id, metadata):
        # Stores metadata for a task
        self.table[task_id] = metadata

    def get_metadata(self, task_id):
        # Retrieves metadata by task ID
        return self.table.get(task_id, {})

    def delete_metadata(self, task_id):
        # Removes metadata associated with a task ID
        if task_id in self.table:
            del self.table[task_id]
