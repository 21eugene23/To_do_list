# reminder_queue.py
# Queue data structure to handle scheduled reminders (FIFO order).

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, reminder):
        # Add a reminder to the queue
        self.queue.append(reminder)

    def dequeue(self):
        # Remove the next scheduled reminder
        return self.queue.popleft() if self.queue else None

    def peek(self):
        # View the next reminder without removing it
        return self.queue[0] if self.queue else None
