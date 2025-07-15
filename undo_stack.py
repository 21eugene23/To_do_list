# undo_stack.py
# Stack data structure to support undo/redo of task actions.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        # Push an action (like add/delete) onto the stack
        self.stack.append(action)

    def pop(self):
        # Remove and return the most recent action
        return self.stack.pop() if self.stack else None

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0
