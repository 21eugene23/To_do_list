

import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'data_structures')))

# Import your Queue class
from PriorityQueue import Queue

# A simple Reminder class for testing purposes
class Reminder:
    def __init__(self, message, time=""):
        self.message = message
        self.time = time


    def __eq__(self, other):
        return isinstance(other, Reminder) and self.message == other.message and self.time == other.time

    def __repr__(self):
        return f"Reminder('{self.message}', '{self.time}')"


def test_queue_enqueue_dequeue_fifo():
    q = Queue()
    reminder1 = Reminder("Buy groceries", "10:00 AM")
    reminder2 = Reminder("Call mom", "11:30 AM")
    reminder3 = Reminder("Project deadline", "05:00 PM")

    q.enqueue(reminder1)
    q.enqueue(reminder2)
    q.enqueue(reminder3)

    # Check FIFO order
    assert q.dequeue() == reminder1
    assert q.dequeue() == reminder2
    assert q.dequeue() == reminder3
    assert q.dequeue() is None # Queue should be empty now

def test_queue_peek():
    q = Queue()
    reminder1 = Reminder("Check emails")
    reminder2 = Reminder("Attend meeting")

    q.enqueue(reminder1)
    assert q.peek() == reminder1 # Peek should return the first item
    assert q.peek() == reminder1 # Peek again, should still be the first item
    assert q.dequeue() == reminder1 # Now remove it

    q.enqueue(reminder2)
    assert q.peek() == reminder2
    assert q.dequeue() == reminder2
    assert q.peek() is None # Queue should be empty

def test_queue_empty_operations():
    q = Queue()
    assert q.dequeue() is None # Dequeue from empty
    assert q.peek() is None    # Peek from empty

def test_queue_size():
    q = Queue()
    assert len(q.queue) == 0

    q.enqueue(Reminder("A"))
    assert len(q.queue) == 1

    q.enqueue(Reminder("B"))
    q.enqueue(Reminder("C"))
    assert len(q.queue) == 3

    q.dequeue()
    assert len(q.queue) == 2

    q.dequeue()
    q.dequeue()
    assert len(q.queue) == 0
    assert q.dequeue() is None