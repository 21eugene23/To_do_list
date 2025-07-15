# tests/test_hash_table_metadata.py

import sys
import os

# Add the src/data_structures directory to Python's path
# This allows pytest to find your HashTable class
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'data_structures')))

# Import your HashTable class
from hash_table import HashTable

def test_hash_table_add_get_metadata():
    ht = HashTable()

    # Test adding and retrieving metadata
    task_id_1 = "task_001"
    metadata_1 = {"priority": 1, "status": "pending", "due_date": "2025-07-16"}
    ht.add_metadata(task_id_1, metadata_1)
    assert ht.get_metadata(task_id_1) == metadata_1

    task_id_2 = "task_002"
    metadata_2 = {"priority": 3, "status": "completed"}
    ht.add_metadata(task_id_2, metadata_2)
    assert ht.get_metadata(task_id_2) == metadata_2

    # Test retrieving non-existent metadata
    assert ht.get_metadata("non_existent_task") == {} # Should return empty dict

def test_hash_table_update_metadata():
    ht = HashTable()
    task_id = "task_003"
    initial_metadata = {"priority": 2, "assigned_to": "Alice"}
    ht.add_metadata(task_id, initial_metadata)
    assert ht.get_metadata(task_id) == initial_metadata

    # Update metadata for the same task_id
    updated_metadata = {"priority": 1, "assigned_to": "Bob", "notes": "Urgent"}
    ht.add_metadata(task_id, updated_metadata) # add_metadata overwrites existing key
    assert ht.get_metadata(task_id) == updated_metadata

def test_hash_table_delete_metadata():
    ht = HashTable()
    task_id_1 = "task_004"
    metadata_1 = {"status": "active"}
    ht.add_metadata(task_id_1, metadata_1)
    assert ht.get_metadata(task_id_1) == metadata_1

    # Delete existing metadata
    ht.delete_metadata(task_id_1)
    assert ht.get_metadata(task_id_1) == {} # Should return empty dict after deletion

    # Test deleting non-existent metadata (should not raise error)
    ht.delete_metadata("non_existent_task_to_delete")
    assert ht.get_metadata("non_existent_task_to_delete") == {}

def test_hash_table_empty():
    ht = HashTable()
    assert ht.get_metadata("any_id") == {}
    ht.delete_metadata("any_id") # Deleting from empty should be fine
