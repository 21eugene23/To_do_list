# linked_list.py
# Manages the task list using a singly linked list.

class TaskNode:
    def __init__(self, task_id, task_name):
        # A single task with ID and name
        self.task_id = task_id
        self.task_name = task_name
        self.next = None

class LinkedList:
    def __init__(self):
        # Head of the linked list
        self.head = None

    def add_task(self, task_id, task_name):
        # Adds a new task to the beginning of the list
        new_node = TaskNode(task_id, task_name)
        new_node.next = self.head
        self.head = new_node

    def delete_task(self, task_id):
        # Removes a task by ID and returns its name
        current = self.head
        prev = None
        while current:
            if current.task_id == task_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return current.task_name
            prev = current
            current = current.next
        return None

    def get_task_name(self, task_id):
        # Finds the name of a task by ID
        current = self.head
        while current:
            if current.task_id == task_id:
                return current.task_name
            current = current.next
        return None

    def get_tasks(self):
        # Returns all tasks in (id, name) format
        tasks = []
        current = self.head
        while current:
            tasks.append((current.task_id, current.task_name))
            current = current.next
        return tasks
